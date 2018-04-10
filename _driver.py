"""PytSite Password Authentication UI Driver
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router, lang as _lang, reg as _reg
from plugins import widget as _widget, form as _form, auth_ui as _auth_ui, assetman as _assetman, auth as _auth

_bs_ver = _reg.get('auth_ui_password.twitter_bootstrap_version', 4)


class _SignInForm(_form.Form):
    """Password Sign In Form
    """

    def _on_setup_form(self, **kwargs):
        """Hook
        """
        self.data['bs-version'] = _bs_ver
        self.area_footer_css = 'text-center'

        _assetman.preload('auth_ui_password@js/form.js')

    def _on_setup_widgets(self):
        """Hook
        """

        self.add_widget(_widget.input.Email(
            uid='login',
            weight=10,
            placeholder=_lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
            value=_router.request().inp.get('login', ''),
        ))

        self.add_widget(_widget.input.Password(
            uid='password',
            weight=20,
            placeholder=_lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
        ))

        if _auth.is_sign_up_enabled():
            sign_up_url = _router.rule_url('auth_ui@sign_up', {'driver': 'password'})
            self.add_widget(_widget.static.Text(
                uid='sign_up_link',
                weight=30,
                title=_lang.t('auth_ui_password@sign_in_form_propose', {'url': sign_up_url}),
                h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
                h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
                css='text-center',
            ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = _lang.t('auth_ui_password@sign_in')
        submit_btn.icon = 'fa fa-sign-in'


class _SignUpForm(_form.Form):
    def _on_setup_form(self, **kwargs):
        """Hook
        """
        self.area_footer_css = 'text-center'

    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(_widget.input.Email(
            uid='login',
            weight=10,
            placeholder=_lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
            value=_router.request().inp.get('login', ''),
        ))

        self.add_widget(_widget.input.Password(
            uid='password',
            weight=20,
            placeholder=_lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Password(
            uid='password_confirm',
            weight=30,
            placeholder=_lang.t('auth_ui_password@password_confirm'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Text(
            uid='first_name',
            weight=40,
            placeholder=_lang.t('auth_ui_password@first_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Text(
            uid='last_name',
            weight=50,
            placeholder=_lang.t('auth_ui_password@last_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            h_size_label=True,
            required=True,
        ))

        sign_in_url = _router.rule_url('auth_ui@sign_in', {'driver': 'password'})
        self.add_widget(_widget.static.Text(
            uid='sign_in_link',
            weight=60,
            title=_lang.t('auth_ui_password@sign_up_form_propose', {'url': sign_in_url}),
            h_size='col col-sm-6' if _bs_ver == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _bs_ver == 4 else '',
            css='text-center',
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = _lang.t('auth_ui_password@sign_up')
        submit_btn.icon = 'fa fa-user-plus'

    def _on_validate(self):
        """Hook
        """
        errors = {}

        try:
            _auth.get_user(self.val('login'))
            errors['login'] = _lang.t('auth_ui_password@login_already_taken')
        except _auth.error.UserNotFound:
            pass

        if self.val('password') != self.val('password_confirm'):
            err_msg = _lang.t('auth_ui_password@passwords_not_match')
            errors.update({
                'password': err_msg,
                'password_confirm': err_msg,
            })

        if errors:
            raise _form.error.ValidationError(errors)


class Password(_auth_ui.Driver):
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

    def get_sign_in_form(self, **kwargs) -> _form.Form:
        """Get the sign in form
        """
        _assetman.preload('twitter-bootstrap-{}'.format(_reg.get('auth_ui_password.twitter_bootstrap_version', 4)))
        _assetman.preload('font-awesome')

        return _SignInForm(**kwargs)

    def get_sign_up_form(self, **kwargs) -> _form.Form:
        """Get the sign up form
        """
        _assetman.preload('twitter-bootstrap-{}'.format(_reg.get('auth_ui_password.twitter_bootstrap_version', 4)))
        _assetman.preload('font-awesome')

        return _SignUpForm(**kwargs)
