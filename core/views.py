from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import AppUser, TaskToDo

def index(request):
    user_is_authenticated = request.user.is_authenticated
    return render(request,'core/index.html', {'user_is_authenticated':user_is_authenticated})

def singup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        error_msg = ''
        user = AppUser.objects.filter(username=username).first()
        if user:
            error_msg = 'Username already in use'
            print(error_msg)
            return render(request, 'core/singup.html')
        else:
            user = AppUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            user  = authenticate(username=username, password=password)
            django_login(request, user)
            
            return redirect('index')
              


        
    else:
        return render(request, 'core/singup.html')