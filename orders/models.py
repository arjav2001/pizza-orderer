from django.db import models

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
            return f"{self.item_type}: {self.name} for ${self.price}"
        return f"{self.item_type}: {self.size} {self.name} for ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if self.price == 0.00:
            return f"{self.name}"
        return f"{self.name} for ${self.price}"

class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.IntegerField()

    def __str__(self):
        if self.toppings is None:
            return f"{self.item}"
        return f"{self.item} with {self.toppings} for ${self.price}"

class Order(models.Model):
    items = models.ManyToManyField(OrderItem, blank=False)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.items}, Total Price:${self.price}"