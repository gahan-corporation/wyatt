"""Setup tools config."""
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='gerp',
    version='0.0.1',
    description='gerp',
    long_description='gerp',
    url='https://github.com/gahan-corporation/gerp',
    author='Gahan Corporation',
    author_email='info@gahan-corporation.com',
    # scripts=['setup/odoo'],
    packages=find_packages(),
    package_dir={'gerp': 'packages'},
    include_package_data=True,
    install_requires=[
        'babel >= 1.0',
        'decorator',
        'docutils',
        'feedparser',
        'gevent',
        'html2text',
        'Jinja2',
        'lxml',  # windows binary http://www.lfd.uci.edu/~gohlke/pythonlibs/
        'mako',
        'mock',
        'ofxparse',
        'passlib',
        'pillow',  # windows binary http://www.lfd.uci.edu/~gohlke/pythonlibs/
        'psutil',  # windows binary code.google.com/p/psutil/downloads/list
        'psycopg2 >= 2.2',
        'pydot',
        'pyldap',  # optional
        'pyparsing',
        'pypdf2',
        'pyserial',
        'python-dateutil',
        'pytz',
        'pyusb >= 1.0.0b1',
        'pyyaml',
        'qrcode',
        'reportlab',  # windows binary pypi.python.org/pypi/reportlab
        'requests',
        'suds-jurko',
        'vatnumber',
        'vobject',
        'werkzeug',
        'xlsxwriter',
        'xlwt',
    ],
    python_requires='>=3.5',
    extras_require={
        'SSL': ['pyopenssl'],
    },
    tests_require=[
        'mock',
        'pytest-runner',
    ],
)
