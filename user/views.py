from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def login(req):
    return render(req, 'login.html')
    pass


def deal_login(req):
    return HttpResponse('username:' + req.POST['username'] + ' password:' + req.POST['password'])
    pass


def register(req):
    return render(req, 'register.html')
    pass


def deal_register(req):
    username = req.POST['username']
    password = req.POST['password']
    new_user = User(username=username, password=password)
    new_user.save()
    return HttpResponse('username:' + username + '<br> password:' + password)
    pass