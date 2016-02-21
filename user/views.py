from django.shortcuts import render
from django.http import HttpResponse
import json
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
    print('deal register')
    print('POST:', req.POST)
    print('GET:', req.GET)
    return HttpResponse("copy")
    # username = req.POST['reName']
    # password = req.POST['password']
    # tel = req.POST['tel']
    # new_user = User(username=username, password=password, tel=tel)
    # new_user.save()
    # return HttpResponse('username:' + username + '<br> password:' + password + '<br> tel:' + tel)
    # print(username)
    pass