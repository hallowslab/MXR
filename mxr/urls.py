from django.urls import path
from . import views

app_name = "mxr"

urlpatterns = [
    path("", views.index, name="mxr_home"),
]
