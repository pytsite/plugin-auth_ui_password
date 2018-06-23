"""PytSite Auth UI Password Plugin Forms
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import reg as _reg, router as _router, lang as _lang, cache as _cache, util as _util, tpl as _tpl, \
    mail as _mail, http as _http
from plugins import form as _form, widget as _widget, auth as _auth

_BS_VER = _reg.get('auth_ui_password.twitter_bootstrap_version', 4)
_RESET_TOKENS_POOL = _cache.get_pool('auth_ui_password.reset_password_tokens')
_RESET_TOKEN_TTL = 86400


class SignIn(_form.Form):
    """Password Sign In Form
    """

    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'
        self.assets.extend([
            'twitter-bootstrap-{}'.format(_BS_VER),
            'font-awesome-4',
        ])

    def _on_setup_widgets(self):
        """Hook
        """

        self.add_widget(_widget.input.Email(
            uid='login',
            weight=10,
            placeholder=_lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=_router.request().inp.get('login', ''),
        ))

        self.add_widget(_widget.input.Password(
            uid='password',
            weight=20,
            placeholder=_lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        if _auth.is_sign_up_enabled():
            sign_up_url = _router.rule_url('auth_ui@sign_up', {'driver': 'password'})
            self.add_widget(_widget.static.Text(
                uid='sign_up_link',
                weight=30,
                title=_lang.t('auth_ui_password@sign_in_form_propose', {'url': sign_up_url}),
                h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
                h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
                css='text-center',
            ))

        reset_pw_url = _router.rule_url('auth_ui@restore_account', {'driver': 'password'})
        self.add_widget(_widget.static.Text(
            uid='reset_pw_link',
            weight=40,
            title=_lang.t('auth_ui_password@reset_password_propose', {'url': reset_pw_url}),
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            css='text-center',
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = _lang.t('auth_ui_password@sign_in')
        submit_btn.icon = 'fa fa-sign-in'


class SignUp(_form.Form):
    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'
        self.assets.extend([
            'twitter-bootstrap-{}'.format(_BS_VER),
            'font-awesome-4',
        ])

    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(_widget.input.Email(
            uid='login',
            weight=10,
            placeholder=_lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=_router.request().inp.get('login', ''),
        ))

        self.add_widget(_widget.input.Password(
            uid='password',
            weight=20,
            placeholder=_lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Password(
            uid='password_confirm',
            weight=30,
            placeholder=_lang.t('auth_ui_password@password_confirm'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Text(
            uid='first_name',
            weight=40,
            placeholder=_lang.t('auth_ui_password@first_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Text(
            uid='last_name',
            weight=50,
            placeholder=_lang.t('auth_ui_password@last_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        sign_in_url = _router.rule_url('auth_ui@sign_in', {'driver': 'password'})
        self.add_widget(_widget.static.Text(
            uid='sign_in_link',
            weight=60,
            title=_lang.t('auth_ui_password@sign_up_form_propose', {'url': sign_in_url}),
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
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
            raise _form.FormValidationError(errors)


class RestoreAccount(_form.Form):
    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'
        self.assets.extend([
            'twitter-bootstrap-{}'.format(_BS_VER),
            'font-awesome-4',
        ])

    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(_widget.input.Email(
            uid='login',
            weight=10,
            placeholder=_lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=_router.request().inp.get('login', ''),
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = _lang.t('auth_ui_password@reset_password')
        submit_btn.icon = 'fa fa-key'

    def _on_submit(self):
        try:
            user = _auth.get_user(self.val('login'))
            if user.status != _auth.USER_STATUS_ACTIVE:
                return

            token = _util.random_password(64, True)
            _RESET_TOKENS_POOL.put(token, user.login, _RESET_TOKEN_TTL)
            reset_url = _router.rule_url('auth_ui_password@reset', {'token': token})
            msg_body = _tpl.render('auth_ui_password@mail/{}/reset-password'.format(_lang.get_current()), {
                'user': user, 'reset_url': reset_url
            })
            _mail.Message(user.login, _lang.t('auth_ui_password@reset_password_mail_subject'), msg_body).send()

            _router.session().add_info_message(_lang.t('auth_ui_password@check_email_for_instructions'))

        except _auth.error.UserNotFound:
            pass


class SetNewPassword(_form.Form):
    def _on_setup_form(self):
        """Hook
        """
        if not _RESET_TOKENS_POOL.has(self.attr('token')):
            raise RuntimeError('Invalid token')

        self.css += ' auth-ui-form'
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'
        self.title = _lang.t('auth_ui_password@reset_password')
        self.assets.extend([
            'twitter-bootstrap-{}'.format(_BS_VER),
            'font-awesome-4',
        ])

    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Password(
            uid='password',
            weight=10,
            placeholder=_lang.t('auth_ui_password@new_password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(_widget.input.Password(
            uid='password_confirm',
            weight=20,
            placeholder=_lang.t('auth_ui_password@password_confirm'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = _lang.t('auth_ui_password@reset_password')
        submit_btn.icon = 'fa fa-key'

    def _on_validate(self):
        """Hook
        """
        if self.val('password') != self.val('password_confirm'):
            err_msg = _lang.t('auth_ui_password@passwords_not_match')
            raise _form.FormValidationError({
                'password': err_msg,
                'password_confirm': err_msg,
            })

    def _on_submit(self):
        """Hook
        """
        try:
            token = self.attr('token')
            user = _auth.get_user(_RESET_TOKENS_POOL.get(token))

            _auth.switch_user_to_system()
            user.password = self.val('password')
            user.save()
            _auth.restore_user()

            _RESET_TOKENS_POOL.rm(token)

            _router.session().add_success_message(_lang.t('auth_ui_password@reset_password_success'))

            return _http.RedirectResponse(_router.rule_url('auth_ui@sign_in', {'driver': 'password'}))

        except _auth.error.UserNotFound:
            raise RuntimeError('Invalid token')
