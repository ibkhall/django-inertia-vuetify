from unicodedata import name
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from inertia import render
from .serializers import LoginSchema
from .models import Category


def login_form(request):
    Category(name="Hello")
    categories = Category.objects.all()
    print(categories)
    return render(request, 'Auth/Login')


def connect(request):
    loginSchema = LoginSchema()
    if request.method=='POST':
        data = loginSchema.loads(request.body)
        print(data)
        username = data['username']
        password = data['password']
        print(username)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
    return HttpResponse("Erreur des identifiants")
