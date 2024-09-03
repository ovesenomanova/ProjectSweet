from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name = 'main'),
    path('contacts/', views.ContactView.as_view(), name = 'contact'),
    path('order/', views.OrderView.as_view(), name = 'order')

]