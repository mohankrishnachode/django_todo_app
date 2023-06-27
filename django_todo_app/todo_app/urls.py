from django.urls import path
from . import views
#app_name = 'todo_app'

urlpatterns = [
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
    path('todo', views.task_list, name='task_list'),
    path('create', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]
