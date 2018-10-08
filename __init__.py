"""PytSite Password Authentication UI Driver Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import cache

    cache.create_pool('auth_ui_password.reset_password_tokens')


def plugin_load_wsgi():
    from pytsite import router
    from plugins import auth_ui
    from . import _driver, _controllers

    auth_ui.register_driver(_driver.Password())
    router.handle(_controllers.ResetPassword, 'auth_ui_password/reset/<token>', 'auth_ui_password@reset')
