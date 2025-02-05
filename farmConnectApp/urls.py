from django.urls import path
from . import views

urlpatterns = [
    path("consumer/signup", views.consumerSignUp, name="consumer_signup")
]
