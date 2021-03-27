from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        print(username, email)
        return render(request, "calorie_counter/index.html", {
            "email": email,
            "username": username,
        })
    else:
        return render(request, "calorie_counter/index.html")


def register(request):
    return HttpResponse("HOLAAAA")
