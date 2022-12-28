# dftc/urls.py

from django.urls import path
from .views import dashboard
from .views import display

app_name = "DownForTheCount"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("display/", display, name='display'),
]