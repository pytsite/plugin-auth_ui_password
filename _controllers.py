"""PytSite Auth UI Password Plugin Controllers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import routing, tpl, metatag
from . import _frm


class ResetPassword(routing.Controller):
    def exec(self):
        form = _frm.SetNewPassword(self.request, token=self.arg('token'))

        metatag.t_set('title', form.title)

        tpl_args = {
            'driver': 'password',
            'form_type': 'reset-password',
            'form': form,
        }

        # Try to render tpl provided by application
        try:
            return tpl.render('auth_ui/form', tpl_args)

        # Render auth_ui plugin's built-in tpl
        except tpl.error.TemplateNotFound:
            return tpl.render('auth_ui@form', tpl_args)
