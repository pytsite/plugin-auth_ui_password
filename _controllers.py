"""PytSite Auth UI Password Plugin Controllers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import routing as _routing, tpl as _tpl, metatag as _metatag
from . import _frm


class ResetPassword(_routing.Controller):
    def exec(self):
        form = _frm.SetNewPassword(self.request, token=self.arg('token'))

        _metatag.t_set('title', form.title)

        tpl_args = {
            'driver': 'password',
            'form_type': 'reset-password',
            'form': form,
        }

        # Try to render tpl provided by application
        try:
            return _tpl.render('auth_ui/form', tpl_args)

        # Render auth_ui plugin's built-in tpl
        except _tpl.error.TemplateNotFound:
            return _tpl.render('auth_ui@form', tpl_args)
