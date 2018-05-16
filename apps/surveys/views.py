from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("<h3>placeholder to display all the surveys created</h3>")


def new(request):
    return HttpResponse("<h3>placeholder for users to add a new survey</h3>")