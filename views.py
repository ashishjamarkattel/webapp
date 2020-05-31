from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def signup(request):

    if request.method =="POST":

        email = request.POST.get("email")

        password = request.POST.get("password")

        username = request.POST.get("username")

        firstname= request.POST.get("first_name")

        lastname = request.POST.get("last_name")

        user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
        user.save()

        return redirect('login/')


    else:
        return render(request,'signup.html')











