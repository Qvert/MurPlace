from django.contrib.auth import authenticate, login as user_login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Profile


def index(request):
    return render(request, "main_page/index.html")


def auth_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        usr = authenticate(request, login, password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, "auth_page/auth.html")

    return render(request, "auth_page/auth.html")


def reg_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:

            Profile.objects.create_user(login, password)

            usr = authenticate(request, login, password)
            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, "auth_page/reg.html")
    return render(request, "auth_page/reg.html")
