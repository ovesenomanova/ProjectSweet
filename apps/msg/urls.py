from django.urls import path
from . import views

urlpatterns = [
    path('', views.MsgView.as_view()),
]