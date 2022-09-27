from django.urls import path
from todolist.views import show_todo, register, login_user, logout_user, ask_todo_creation

app_name = 'todolist'

urlpatterns = [
    path('', show_todo, name='show_todo'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', ask_todo_creation, name='ask_todo_creation')
]