from .. import views
from .. import forms


class EmailRecover(views.Recover):
    search_fields = ['email']
email_recover = EmailRecover.as_view(form_class=forms.PasswordRecoveryForm)


class UsernameRecover(views.Recover):
    search_fields = ['username']
username_recover = UsernameRecover.as_view(form_class=forms.PasswordRecoveryForm)
