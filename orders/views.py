from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
        "user": request.user
    }
    return render(request, "orders/homepage.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message" : "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def sign_up(request):
    return render(request, "orders/sign_up.html", {})

def sign_up_verification(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    return render(request, "orders/homepage.html", {"user": user})
