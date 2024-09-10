from django.urls import path
from . import views

urlpatterns = [
    path('new-message/', views.ForumMessageView.as_view(), name='new_post'),
    path('all-messages/', views.ForumView.as_view(), name='all'),
]
