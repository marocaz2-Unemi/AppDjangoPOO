from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('about/', views.about),
    path('home/<str:username>/', views.home), 
    path('projects/', views.projects),
    path('tasks/', views.tasks)
 
]
