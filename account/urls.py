from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from account.views import *


urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("perfil/", profile_detail, name="perfil_detail"),
    path("perfil/change", profile_change, name="perfil_change"),
]