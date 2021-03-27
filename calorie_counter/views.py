from django.shortcuts import render
from django.http import HttpResponse
from logic import .


def index(request):
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data['email']
    return render(request, "calorie_counter/index.html", {
        "email": email,
        "username": username,
    })


def register(request):
    return HttpResponse("HOLAAAA")
