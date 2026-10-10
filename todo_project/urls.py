"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import task_list, edit_task, toggle_task, delete_task



urlpatterns = [
    path('admin/', admin.site.urls),
 
   path('todo/', task_list, name='task_list'),

path('todo/edit/<int:task_id>/', edit_task, name='edit_task'),
path('todo/toggle/<int:task_id>/', toggle_task, name='toggle_task'),
path('todo/delete/<int:task_id>/', delete_task, name='delete_task'),
]

