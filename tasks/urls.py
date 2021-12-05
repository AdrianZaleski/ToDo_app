from django.urls import path

from .views import TaskList, DetailView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', DetailView.as_view(), name='task'),

    ]
