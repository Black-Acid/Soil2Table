from django.urls import path
from . import views

urlpatterns = [
    path("consumer/signup", views.ConsumerSignUP.as_view(), name="consumer_signup")
]
