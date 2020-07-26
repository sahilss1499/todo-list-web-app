
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    #use this pk variable only in views to make objects
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
