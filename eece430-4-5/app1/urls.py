from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_videos, name='list_videos'),
    path('add/', views.add_video, name='add_video'),
    path('update/<int:pk>/', views.update_video, name='update_video'),
    path('delete/<int:pk>/', views.delete_video, name='delete_video'),
]
