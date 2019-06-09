from django.conf.urls import url
from .views import home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'home$', home, name='user_home'),
    url(r'login$', LoginView.as_view(template_name='registration/login.html'), name='user_login'),
    url(r'logout$', LogoutView.as_view(), name='user_logout')
]
