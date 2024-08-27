from django.urls import path
from . import views


urlpatterns = [
    path('', views.CakesListView.as_view(), name='catalog'),
]