"""PytSite Password Authentication UI Driver
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import http
from plugins import form, auth_ui
from . import _frm


class Password(auth_ui.Driver):
    """Password Authentication UI Driver
    """

    def get_name(self) -> str:
        """Get name of the driver
        """
        return 'password'

    def get_description(self) -> str:
        """Get name of the driver
        """
        return 'Password'

    def get_sign_in_form(self, request: http.Request, **kwargs) -> form.Form:
        """Get the sign in form
        """
        return _frm.SignIn(request, **kwargs)

    def get_sign_up_form(self, request: http.Request, **kwargs) -> form.Form:
        """Get the sign up form
        """
        return _frm.SignUp(request, **kwargs)

    def get_restore_account_form(self, request: http.Request, **kwargs):
        """Get account restoration form
        """
        return _frm.RestoreAccount(request, **kwargs)
