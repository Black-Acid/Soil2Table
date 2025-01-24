from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("testing_data", views.dummy_data, name="dummy_data")
]
