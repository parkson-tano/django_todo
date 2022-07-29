from unicodedata import name
from django.urls import path
from .views import IndexView, ManageView

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("done/<int:pk>", ManageView.as_view(), name='done')
]
