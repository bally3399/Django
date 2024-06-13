from django.shortcuts import render, HttpResponse


# Create your views here.

def say_hello(request, name):
    return HttpResponse(f"Welcome {name}")


def welcome(request, name):
    return render(request, "index.html", context={name: name})
