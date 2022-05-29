# pylint: disable=no-member
'''
  Sales urls.
'''
from django.urls import path
from . import views


app_name = "sales"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
