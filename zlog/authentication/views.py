from django.shortcuts import (
    render,
    redirect,
    HttpResponse
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
