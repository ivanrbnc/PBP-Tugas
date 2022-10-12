import datetime
from todolist.models import Todolist_Data
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def show_todo(request):
    data_todo = Todolist_Data.objects.filter(user = request.user)
    context = {
    'query_set_todo': data_todo,
    'name': request.user,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account creation is success!')
            return redirect('todolist:login')
        else:
            messages.info(request, 'Invalid input!')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todo")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Incorrect Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def ask_todo_creation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Membuat To Do List berdasarkan input user
        todo = Todolist_Data.objects.create(title = title, description = description,date = datetime.date.today(), user = request.user)
        
        # Kembali ke halaman To Do List
        response = HttpResponseRedirect(reverse("todolist:show_todo")) 
        return response

    return render(request, "create.html")

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todolist_Data.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)
        todo.save()
    
        return HttpResponse("CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def show_json(request):
    user = request.user
    data = Todolist_Data.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")