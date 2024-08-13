from django.urls import path
from . import views


urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('r/', views.CakesListView.as_view(), name='list'),
]