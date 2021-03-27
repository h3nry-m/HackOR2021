from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        workout = request.POST['workout']
        return render(request, "calorie_counter/index.html", {
            "email": email,
            "username": username,
            "workout": workout,
        })
    else:
        return render(request, "calorie_counter/index.html")


def register(request):
    return HttpResponse("HOLAAAA")
