from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_up_verification", views.sign_up_verification, name="sign_up_verification")
]
