from django.conf.urls.defaults import url, patterns
from .forms import PasswordRecoveryForm, PasswordResetForm

from . import views


urlpatterns = patterns('',
    url(r'^recover/$', views.Recover.as_view(form_class=PasswordRecoveryForm), name='password_reset_recover'),
    url(r'^reset/done/$', views.reset_done, name='password_reset_done'),
    url(r'^reset/(?P<token>[\w:-]+)/$', views.Reset.as_view(form_class=PasswordResetForm),
        name='password_reset_reset'),
)
