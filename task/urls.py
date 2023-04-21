from django.urls import path
from . import views

app_name = 'task'

# urlpatterns = [
# path('', views.task_list, name='task_list'),
# path('create/', views.task_create, name='task_create'),
# path('<int:pk>/update/', views.task_update, name='task_update'),
# path('<int:pk>/delete/', views.task_delete, name='task_delete'),
# ]

# from django.urls import path
# from .views import user_login, task_list, task_create, task_update, task_delete

# app_name = 'tasks'

urlpatterns = [
    path('', views.get_name, name='user_login'),
    path('logout/', views.log_out, name='logout'),
    path('<int:pk>/list/', views.list_tasks, name='task_list'),
    # path('tasks/', views.task_list, name='task_list'),
    path('<int:u_pk>/create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_edit, name='task_edit'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
