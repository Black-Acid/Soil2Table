from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignUp.as_view(), name=""),
    path("consumer/signup", views.ConsumerSignUP.as_view(), name="consumer_signup")
]
