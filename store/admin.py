from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "price", "category"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# username = hichem, email = hichembrahimi@hotmail.fr, password = Dubai@2021
