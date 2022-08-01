from setuptools import setup

setup(
    name='odoo-addons-themes',
    setup_requires=['setuptools-odoo'],
    odoo_addons={
        'odoo_version_override': '15.0',
    },
)
