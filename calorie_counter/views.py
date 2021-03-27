from django.shortcuts import render
from django.http import HttpResponse
from logic import .


def index(request):
    return render(request, "calorie_counter/index.html", {
        "test": BMR(20),
    })


def register(request):
    return HttpResponse("HOLAAAA")
