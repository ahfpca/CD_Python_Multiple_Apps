from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("<h3>placeholder to later display all the list of users</h3>")


def register(request):
    return HttpResponse("<h3>placeholder for users to create a new user record</h3>")


def login(request):
    return HttpResponse("<h3>placeholder for users to login</h3>")
        

def new(request):
    return redirect("/users/register")