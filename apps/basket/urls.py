from django.urls import path
from . import views

urlpatterns = [
    path('buy/<slug:id>/', views.AddToBinView.as_view(), name='add_to_bin'),
]