"""PytSite Password Authentication UI Driver Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from plugins import assetman

    assetman.register_package(__name__)
    assetman.t_js(__name__ + '@**')

def plugin_install():
    from plugins import assetman

    assetman.build(__name__)


def plugin_load_wsgi():
    from pytsite import lang
    from plugins import auth_ui
    from . import _driver

    lang.register_package(__name__)
    auth_ui.register_driver(_driver.Password())
