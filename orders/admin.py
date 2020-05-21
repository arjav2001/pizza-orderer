from django.contrib import admin
from .models import Topping, MenuItem, ItemType, OrderItem, Order, Size

# Register your models here.
admin.site.register(Topping)
admin.site.register(MenuItem)
admin.site.register(ItemType)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Size)