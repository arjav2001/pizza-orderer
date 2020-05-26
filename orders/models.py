from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemType(models.Model):
    name = models.CharField(max_length=64)

    def __str__ (self):
        return f"{self.name}"

class Size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class MenuItem(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    num_toppings = models.IntegerField()

    def __str__(self):
        if self.size.size == "NA":
            return f"{self.name} for ${self.price}"
        return f"{self.size} {self.name} for ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if self.price == 0.00:
            return f"{self.name}"
        return f"{self.name} for ${self.price}"

class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.item} for ${self.price}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(OrderItem, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Total Price:${self.price}"