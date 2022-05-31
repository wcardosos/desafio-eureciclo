# pylint: disable=no-member,import-error
'''
  Sales urls.
'''
from django.urls import path
from . import views


app_name = "sales"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.SalesListView.as_view(), name="list"),
    path("import/", views.ImportView.as_view(), name="import"),
    path(
      "import/processing/",
      views.ProcessingView.as_view(),
      name="processing"
    ),
    path("import/processing/result", views.ResultView.as_view(), name="result")
]
