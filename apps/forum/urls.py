from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum_index'),
    path('new_post/', views.new_post, name='new_post'),
    path('all/', views.all, name='all')
]
