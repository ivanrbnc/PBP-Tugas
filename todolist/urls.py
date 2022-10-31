from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todo, name='show_todo'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', ask_todo_creation, name='ask_todo_creation'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
    path('delete/<str:id>', delete_task, name='delete_task'),
]