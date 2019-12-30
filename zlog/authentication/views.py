from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# Create your views here.


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user_existance = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse('invalid username')
        user = authenticate(username=username, password=pwd)
        if user is None:
            return HttpResponse('invalid password')
        else:
            login(request, user)
            return HttpResponse(request.user.username)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse('Successfully Logged You Out Sir!')
    else:
        return HttpResponse('Invalid Method')


def register_view(request):
    if request.method == 'GET':
        reg_form = UserRegistrationForm()
        return render(request, 'register.html', context={'reg_form': reg_form})
    else:
        reg_form = UserRegistrationForm(data=request.POST)
        if reg_form.is_valid():
            saved_user = reg_form.save()
            user = authenticate(username=saved_user.username, password=saved_user.password)
            if user is None:
                return HttpResponse('invalid Login')
            else:
                login(request, user)
                return HttpResponse(request.user.username)



