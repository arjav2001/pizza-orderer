from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem, ItemType, Order, OrderItem, Topping

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
        "user": request.user,
        "items": MenuItem.objects.all(),
        "itemTypes": ItemType.objects.all()
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
    order = Order(user=user, ordered=False, price=0)
    order.save()
    return render(request, "orders/homepage.html", {"user": user})

def order_page(request):
    context = {
        "itemTypes": ItemType.objects.all(),
        "items": MenuItem.objects.all()
    }
    return render(request, "orders/order_page.html", context)

def item_order(request, item_id):
    item = MenuItem.objects.get(pk=item_id)
    context = {
        "item": item,
        "toppings": Topping.objects.all()
    }
    return render(request, "orders/item_order.html", context)

def enter_shopping_cart(request):
    toppings_ids = request.POST["to_change"]
    toppings = []
    for toppings_id in toppings_ids:
        toppings.append(Topping.objects.get(pk=int(toppings_id)))
    item_id = request.POST["item"]
    item = MenuItem.objects.get(pk=item_id)
    totalPrice = item.price
    for topping in toppings:
        totalPrice += topping.price
    user = request.user
    orderItem = OrderItem(item=item, price=totalPrice)
    orderItem.save()
    for topping in toppings:
        orderItem.toppings.add(topping)
    orderItem.save()
    order = Order.objects.get(user=user, ordered=False)
    order.items.add(orderItem)
    order.price += orderItem.price
    order.save()
    return render(request, "orders/shopping_cart.html", {"order": order, "toppings":toppings})

