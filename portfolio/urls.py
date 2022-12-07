from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path("paginas/", views.paginas.as_view(), name="paginas"),
    path("", views.Index.as_view(), name="index"),

    path("accounts/login/", LoginView.as_view(), name="login"),
    path('register/', views.SignUp.as_view(), name='register'),
    path('logout/', logout_then_login, name="logout"),

    path('main_page/', views.Main_page.as_view(), name='main'),
    path('project/', views.CreateProject.as_view(), name='create_project'),
]
