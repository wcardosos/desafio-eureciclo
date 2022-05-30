# pylint: disable=no-member,import-error
'''
  Sales urls.
'''
from django.urls import path
from . import views


app_name = "sales"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("processing/", views.ProcessingView.as_view(), name="processing"),
    path("processing/result", views.ResultView.as_view(), name="result")
]
