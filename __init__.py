"""PytSite Password Authentication UI Driver Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import cache
    from plugins import assetman

    cache.create_pool('auth_ui_password.reset_password_tokens')

    assetman.register_package(__name__)
    assetman.t_js(__name__, babelify=True)


def plugin_install():
    from plugins import assetman

    assetman.build(__name__)


def plugin_load_wsgi():
    from pytsite import lang, tpl, router
    from plugins import auth_ui
    from . import _driver, _controllers

    lang.register_package(__name__)
    tpl.register_package(__name__)
    auth_ui.register_driver(_driver.Password())
    router.handle(_controllers.ResetPassword, 'auth_ui_password/reset/<token>', 'auth_ui_password@reset')
