from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import task_list, task_create, task_edit, task_delete

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/new', task_create, name='task_create'),
    path('tasks/edit/<int:task_id>/', task_edit, name='task_edit'),
    path('tasks/delete/<int:task_id>/', task_delete, name='task_delete'),
    path('logout/', LogoutView.as_view(), name='logout')
]
