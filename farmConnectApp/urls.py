from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignUp.as_view(), name=""),
    path("register", views.RegisterUser.as_view(), name="register_user"),
    path("login", views.LoginView.as_view(), name="login")
]
