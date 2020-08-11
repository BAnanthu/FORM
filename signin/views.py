from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == "POST":
        login_name = request.POST['login_name']
        login_password = request.POST['login_password']

        user = auth.authenticate(username=login_name,password=login_password)

        if user is not None:
            auth.login(request,user)
            return render(request,'account/welcome.html')
        else:
            return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'account/welcome.html')