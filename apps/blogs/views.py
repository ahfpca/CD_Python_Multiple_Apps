from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("<h3>placeholder to later display all the list of blog</h3>")


def show(request, id):
    return HttpResponse(f"<h3>placeholder to display blog {id}</h3>")


def new(request):
    return HttpResponse("<h3>placeholder to display a new form to create a new blog</h3>")


def create(request):
    return redirect("/blogs")


def edit(request, id):
    return HttpResponse(f"<h3>placeholder to edit blog {id}</h3>")


def destroy(request, id):
    return redirect("/blogs")
