from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path("", views.Index.as_view(), name="index"),

    path("accounts/login/", LoginView.as_view(), name="login"),
    path('register/', views.SignUp.as_view(), name='register'),
    path('logout/', logout_then_login, name="logout"),

    path('main/', views.Main.as_view(), name='main'),
]
