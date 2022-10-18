from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.tasks_api),
    path('tasks/<int:id>/', views.tasks_api),
    path('notes/', views.notes_api),
    path('notes/<int:id>/', views.notes_api),
]