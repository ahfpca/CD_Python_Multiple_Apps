from django.shortcuts import render, HttpResponse, redirect


def index(request):
    tag = ("<h1>Welcome to Multiple Apps</h1>" 
          "<br>" 
          "<br>"
          "<h2>Please select the app:</h2>"
          "<a href='/blogs'>Blogs</a>"
          "<br>"
          "<a href='/surveys'>Surveys</a>"
          "<br>"
          "<a href='/users'>Users</a>")

    return HttpResponse(tag)
