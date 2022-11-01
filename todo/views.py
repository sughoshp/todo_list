from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myUser = User.objects.create_user(
            username, email, pass1)
        myUser.first_name = firstname
        myUser.last_name = lastname
        myUser.save()
        return redirect('home')
    return render(request, 'signup.html')
def signin(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            fname = user.first_name
            lname = user.last_name
            name = {'fname' : fname , 'Lname' : lname}
            login(request,user)
            return render(request, 'task.html', name)
    return render(request, 'signin.html')
def show_tasks(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home.html')
    context = {}
    task_list = Todo.objects.filter(user = user)
    print(task_list)
    context["task_list"] = list(task_list)
    return render(request, 'show_task.html' , context)
    # return HttpResponse('TaskShown♥')
def signout(request):
    logout(request)
    return render(request, 'home.html')
def create_tasks(request):
    if request.method == 'POST':
        notes = Todo()
        notes.user = request.user
        notes.task = request.POST['task']
        notes.completed = False
        notes.save()
        return redirect('create_tasks')
    return render(request, 'create_task.html')