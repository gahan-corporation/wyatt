# -*- coding: utf-8 -*-
"""Google Drive integration."""
import logging
import json
import re

import requests

import gerp
from gerp.exceptions import RedirectWarning, UserError
from gerp.tools.safe_eval import safe_eval
from gerp.tools.translate import _

#   GOOGLE_TOKEN_ENDPOINT, TIMEOUT)


class GoogleDrive(gerp.models.Model):
    """Class for integration of Google Drive"""
    _name = 'google.drive.config'
    _description = "Google Drive templates config"
    logger = logging.getLogger(__name__)
    word = []
    scope = ''

    @gerp.api.multi
    def get_google_drive_url(self, res_id, template_id):
        """Returns the google drive url."""
        self.ensure_one()
        self = self.sudo()

        model = self.model_id
        filter_name = self.filter_id.name if self.filter_id else False
        record = self.env[model.model].browse(res_id).read()[0]
        record.update({
            'model': model.name,
            'filter': filter_name
        })
        name_gdocs = self.name_template
        try:
            name_gdocs = name_gdocs % record
        except gerp.exceptions.UserError:
            raise gerp.exceptions.UserError(_(
                "At least one key cannot be "
                "found in your Google Drive name pattern"))

        attachments = self.env["ir.attachment"].search([
            ('res_model', '=', model.model),
            ('name', '=', name_gdocs),
            ('res_id', '=', res_id)])
        url = False
        if attachments:
            url = attachments[0].url
        else:
            url = self.copy_doc(res_id, template_id,
                                name_gdocs, model.model).get('url')
        return url

    @gerp.api.model
    def get_access_token(self, scope=None):
        """Get Google Drive access token."""
        config = self.env[
            'ir.config_parameter'].sudo()
        google_drive_refresh_token = config.get_param(
            'google_drive_refresh_token')
        """
        if not google_drive_refresh_token:
            dummy, action_id = self.env['ir.model.data'].get_object_reference(
                'base_setup',
                'action_general_configuration')
            msg = _(
                "You haven't configured 'Authorization Code' "
                "generated from google, Please generate and "
                "configure it .")
            raise RedirectWarning(msg, action_id, _(
                'Go to the configuration panel'))
        else:
            raise UserError(_(
                "Google Drive is not yet configured. "
                "Please contact your administrator."))
        """
        google_drive_client_id = config.get_param('google_drive_client_id')
        google_drive_client_secret = config.get_param(
            'google_drive_client_secret')
        # For Getting New Access Token With help of old Refresh Token
        data = {
            'client_id': google_drive_client_id,
            'refresh_token': google_drive_refresh_token,
            'client_secret': google_drive_client_secret,
            'grant_type': "refresh_token",
            'scope': scope or 'https://www.googleapis.com/auth/drive'
        }
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        try:
            req = requests.post(
                (
                    "https://www.googleapis.com/drive/v3"
                    "/changes/startPageToken?key="),
                data=data,
                headers=headers,
                timeout=60)
            req.raise_for_status()
        except requests.HTTPError:
            dummy, action_id = self.env[
                'ir.model.data'
            ].get_object_reference(
                'base_setup', 'action_general_configuration')
            msg = _(
                "Something went wrong during the token generation. "
                "Please request again an authorization code .")
            raise RedirectWarning(msg, action_id, _(
                'Go to the configuration panel'))
        return req.json().get('access_token')

    @gerp.api.model
    def copy_doc(self, res_id, template_id, name_gdocs, res_model):
        """Copy a doc."""
        google_web_base_url = self.env[
            'ir.config_parameter'].sudo().get_param('web.base.url')
        # Copy template in to drive with help of new access token
        request_url = (
            "https://www.googleapis.com/drive/v2/files/{template_id}?fields="
            "parents/id&access_token={access_token}".format(
                template_id=template_id, access_token=self.get_access_token())
        )
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        try:
            req = requests.post(request_url, headers=headers, timeout=60)
            req.raise_for_status()
            parents_dict = req.json()
        except requests.HTTPError:
            raise UserError(_(
                "The Google Template cannot be found. "
                "Maybe it has been deleted."))

        record_url = (
            "Click on link to open Record in "
            "Odoo\n %s/?db=%s#id=%s&model=%s" % (
                google_web_base_url, self._cr.dbname, res_id, res_model)
        )
        data = {
            "title": name_gdocs,
            "description": record_url,
            "parents": parents_dict['parents']
        }
        request_url = (
            "https://www.googleapis.com/drive/v2/files/{template_id}"
            "/copy?access_token={access_token}".format(
                template_id=template_id, access_token=self.get_access_token())
        )
        headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
        # resp, content = Http().request(request_url,
        # "POST", data_json, headers)
        req = requests.post(request_url, data=json.dumps(
            data), headers=headers, timeout=60)
        req.raise_for_status()
        content = req.json()
        res = {}
        if content.get('alternateLink'):
            res['id'] = self.env["ir.attachment"].create({
                'res_model': res_model,
                'name': name_gdocs,
                'res_id': res_id,
                'type': 'url',
                'url': content['alternateLink']
            }).id
            # Commit in order to attach the document to the current object
            # instance, even if the permissions has not been written.
            self._cr.commit()
            res['url'] = content['alternateLink']
            key = self._get_key_from_url(res['url'])
            request_url = (
                "https://www.googleapis.com/drive/v2/files/{key}/permissions"
                "?emailMessage=This+is+a+drive+file+created+by+Odoo&sendNoti"
                "ficationEmails=false&access_token={access_token}".format(
                    key=key, access_token=self.get_access_token())
            )
            data = {'role': 'writer', 'type': 'anyone',
                    'value': '', 'withLink': True}
            try:
                req = requests.post(request_url, data=json.dumps(
                    data), headers=headers, timeout=60)
                req.raise_for_status()
            except requests.HTTPError:
                raise self.env['res.config.settings'].get_config_warning(_(
                    "The permission 'reader' for 'anyone with the link' "
                    "has not been written on the document"))
            if self.env.user.email:
                data = {'role': 'writer', 'type': 'user',
                        'value': self.env.user.email}
                try:
                    requests.post(request_url, data=json.dumps(
                        data), headers=headers, timeout=60)
                except requests.HTTPError:
                    pass
        return res

    @gerp.api.model
    def get_google_drive_config(self, res_model, res_id):
        """
        Function called by the js, when no google doc are
        yet associated with a record, with the aim to create one. It
        will first seek for a google.docs.config associated with
        the model `res_model` to find out what's the template
        of google doc to copy (this is usefull if you want
        to start with a non-empty document, a type or a name
        different than the default values). If no config is associated with
        the `res_model`, then a blank text document
        with a default name is created.
          :param res_model: the object for which the google doc is created
          :param ids: the list of ids of the objects for which the google doc
                is created. This list is supposed to have
            a length of 1 element only (batch processing is not
            supported in the code, though nothing really prevent it)
          :return: the config id and config name
        """
        if not res_id:
            raise UserError(
                _("Creating google drive may only be done by one at a time."))
        # check if a model is configured with a template
        configs = self.search([('model_id', '=', res_model)])
        config_values = []
        for config in configs.sudo():
            if config.filter_id:
                if (config.filter_id.user_id and
                        config.filter_id.user_id.id != self.env.user.id):
                    # Private
                    continue
                domain = [('id', 'in', [res_id])] + \
                    safe_eval(config.filter_id.domain)
                additionnal_context = safe_eval(config.filter_id.context)
                google_doc_configs = self.env[
                    config.filter_id.model_id].with_context(
                        **additionnal_context).search(domain)
                if google_doc_configs:
                    config_values.append(
                        {'id': config.id, 'name': config.name})
            else:
                config_values.append({'id': config.id, 'name': config.name})
        return config_values

    name = gerp.fields.Char('Template Name', required=True)
    model_id = gerp.fields.Many2one(
        'ir.model', 'Model', ondelete='set null', required=True)
    model = gerp.fields.Char(
        'Related Model', related='model_id.model', readonly=True)
    filter_id = gerp.fields.Many2one(
        'ir.filters', 'Filter', domain="[('model_id', '=', model)]")
    google_drive_template_url = gerp.fields.Char('Template URL', required=True)
    google_drive_resource_id = gerp.fields.Char(
        'Resource Id', compute='_compute_ressource_id')
    google_drive_client_id = gerp.fields.Char(
        'Google Client', compute='_compute_client_id')
    name_template = gerp.fields.Char(
        'Google Drive Name Pattern',
        default='Document %(name)s',
        help=(
            "Choose how the new google drive will "
            "be named, on google side. Eg. "
            "gdoc_%(field_name)s"
        ),
        required=True)
    active = gerp.fields.Boolean('Active', default=True)

    def _get_key_from_url(self, url):
        """Take access key from url."""
        self.word = re.search("(key=|/d/)([A-Za-z0-9-_]+)", url)
        if self.word:
            return self.word.group(2)
        return None

    @gerp.api.multi
    def _compute_ressource_id(self):
        result = {}
        for record in self:
            word = self._get_key_from_url(record.google_drive_template_url)
            if word:
                record.google_drive_resource_id = word
            else:
                raise UserError(_("Please enter a valid Google Document URL."))
        return result

    @gerp.api.multi
    def _compute_client_id(self):
        google_drive_client_id = self.env['ir.config_parameter'].sudo(
        ).get_param('google_drive_client_id')
        for record in self:
            record.google_drive_client_id = google_drive_client_id

    @gerp.api.onchange('model_id')
    def _onchange_model_id(self):
        if self.model_id:
            self.model = self.model_id.model
        else:
            self.filter_id = False
            self.model = False

    def get_google_scope(self):
        """This gets the google scope."""
        self.scope = (
            "https://www.googleapis.com/auth/drive "
            "https://www.googleapis.com/auth/drive.file")
        return self.scope
