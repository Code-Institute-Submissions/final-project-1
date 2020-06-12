from django.conf.urls import url
from django.urls import reverse_lazy, path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path(
        '',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'done/',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        r'(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
        PasswordResetConfirmView.as_view(),
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'
    ),
    path(
        'complete/',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
