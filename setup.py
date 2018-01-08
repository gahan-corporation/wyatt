"""Setup tools config."""
# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    author='Gahan Corporation',
    author_email='info@gahan-corporation.com',
    description='gerp',
    extras_require={
        'SSL': ['pyopenssl'],
    },
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
    long_description='gerp',
    name='gerp',
    packages=[
        'addons/account',
        'addons/backend_theme_v11',
        'addons/hr',
        'addons/sale',
        'addons/web',
        'gerp/addons/base',
    
    ],
    python_requires='>=3.5',
    tests_require=[
        'pytest-runner',
    ],
    url='https://github.com/gahan-corporation/gerp',
    version='0.0.1',
)
