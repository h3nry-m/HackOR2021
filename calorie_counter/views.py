from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "calorie_counter/index.html")


def register(request):
    return HttpResponse("HOLAAAA")
