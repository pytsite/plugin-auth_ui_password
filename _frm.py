"""PytSite Auth UI Password Plugin Forms
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import reg, router, lang, cache, util, tpl, mail
from plugins import form, widget, auth

_BS_VER = reg.get('auth_ui_password.twitter_bootstrap_version', 4)
_RESET_TOKENS_POOL = cache.get_pool('auth_ui_password.reset_password_tokens')
_RESET_TOKEN_TTL = 86400


class SignIn(form.Form):
    """Password Sign In Form
    """

    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'

    def _on_setup_widgets(self):
        """Hook
        """

        self.add_widget(widget.input.Email(
            uid='login',
            weight=10,
            placeholder=lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=router.request().inp.get('login', ''),
        ))

        self.add_widget(widget.input.Password(
            uid='password',
            weight=20,
            placeholder=lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        if auth.is_sign_up_enabled():
            sign_up_url = router.rule_url('auth_ui@sign_up', {'driver': 'password'})
            self.add_widget(widget.static.Text(
                uid='sign_up_link',
                weight=30,
                text=lang.t('auth_ui_password@sign_in_form_propose', {'url': sign_up_url}),
                h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
                h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
                css='text-center',
            ))

        reset_pw_url = router.rule_url('auth_ui@restore_account', {'driver': 'password'})
        self.add_widget(widget.static.Text(
            uid='reset_pw_link',
            weight=40,
            text=lang.t('auth_ui_password@reset_password_propose', {'url': reset_pw_url}),
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            css='text-center',
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = lang.t('auth_ui_password@sign_in')
        submit_btn.icon = 'fa fa-sign-in'


class SignUp(form.Form):
    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'

    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(widget.input.Email(
            uid='login',
            weight=10,
            placeholder=lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=router.request().inp.get('login', ''),
        ))

        self.add_widget(widget.input.Password(
            uid='password',
            weight=20,
            placeholder=lang.t('auth_ui_password@password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(widget.input.Password(
            uid='password_confirm',
            weight=30,
            placeholder=lang.t('auth_ui_password@password_confirm'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(widget.input.Text(
            uid='first_name',
            weight=40,
            placeholder=lang.t('auth_ui_password@first_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(widget.input.Text(
            uid='last_name',
            weight=50,
            placeholder=lang.t('auth_ui_password@last_name'),
            prepend='<i class="fa fa-fw fa-address-book"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        sign_in_url = router.rule_url('auth_ui@sign_in', {'driver': 'password'})
        self.add_widget(widget.static.Text(
            uid='sign_in_link',
            weight=60,
            text=lang.t('auth_ui_password@sign_up_form_propose', {'url': sign_in_url}),
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            css='text-center',
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = lang.t('auth_ui_password@sign_up')
        submit_btn.icon = 'fa fa-user-plus'

    def _on_validate(self):
        """Hook
        """
        errors = {}

        try:
            auth.get_user(self.val('login'))
            errors['login'] = lang.t('auth_ui_password@login_already_taken')
        except auth.error.UserNotFound:
            pass

        if self.val('password') != self.val('password_confirm'):
            err_msg = lang.t('auth_ui_password@passwords_not_match')
            errors.update({
                'password': err_msg,
                'password_confirm': err_msg,
            })

        if errors:
            raise form.FormValidationError(errors)


class RestoreAccount(form.Form):
    def _on_setup_form(self):
        """Hook
        """
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'

    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(widget.input.Email(
            uid='login',
            weight=10,
            placeholder=lang.t('auth_ui_password@email'),
            prepend='<i class="fa fa-fw fa-envelope"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
            value=router.request().inp.get('login', ''),
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = lang.t('auth_ui_password@reset_password')
        submit_btn.icon = 'fa fa-key'

    def _on_submit(self):
        try:
            user = auth.get_user(self.val('login'))
            if user.status != auth.USER_STATUS_ACTIVE:
                return

            token = util.random_password(64, True)
            _RESET_TOKENS_POOL.put(token, user.login, _RESET_TOKEN_TTL)
            reset_url = router.rule_url('auth_ui_password@reset', {'token': token})
            msg_body = tpl.render('auth_ui_password@mail/{}/reset-password'.format(lang.get_current()), {
                'user': user, 'reset_url': reset_url
            })
            mail.Message(user.login, lang.t('auth_ui_password@reset_password_mail_subject'), msg_body).send()

            router.session().add_info_message(lang.t('auth_ui_password@check_email_for_instructions'))

        except auth.error.UserNotFound:
            pass


class SetNewPassword(form.Form):
    def _on_setup_form(self):
        """Hook
        """
        if not _RESET_TOKENS_POOL.has(self.attr('token')):
            raise RuntimeError('Invalid token')

        self.css += ' auth-ui-form'
        self.title_css = 'text-center'
        self.area_footer_css = 'text-center'
        self.title = lang.t('auth_ui_password@reset_password')

    def _on_setup_widgets(self):
        self.add_widget(widget.input.Password(
            uid='password',
            weight=10,
            placeholder=lang.t('auth_ui_password@new_password'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        self.add_widget(widget.input.Password(
            uid='password_confirm',
            weight=20,
            placeholder=lang.t('auth_ui_password@password_confirm'),
            prepend='<i class="fa fa-fw fa-lock"></i>',
            h_size='col col-sm-6' if _BS_VER == 4 else 'col-sm-6 col-sm-offset-3',
            h_size_row_css='justify-content-center' if _BS_VER == 4 else '',
            h_size_label=True,
            required=True,
        ))

        submit_btn = self.get_widget('action_submit')
        submit_btn.value = lang.t('auth_ui_password@reset_password')
        submit_btn.icon = 'fa fa-key'

    def _on_validate(self):
        """Hook
        """
        if self.val('password') != self.val('password_confirm'):
            err_msg = lang.t('auth_ui_password@passwords_not_match')
            raise form.FormValidationError({
                'password': err_msg,
                'password_confirm': err_msg,
            })

    def _on_submit(self):
        """Hook
        """
        try:
            token = self.attr('token')
            user = auth.get_user(_RESET_TOKENS_POOL.get(token))

            auth.switch_user_to_system()
            user.password = self.val('password')
            user.save()
            auth.restore_user()

            _RESET_TOKENS_POOL.rm(token)

            router.session().add_success_message(lang.t('auth_ui_password@reset_password_success'))

            self.redirect = router.rule_url('auth_ui@sign_in', {'driver': 'password'})

        except auth.error.UserNotFound:
            raise RuntimeError('Invalid token')
