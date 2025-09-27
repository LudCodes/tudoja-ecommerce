# cadastrar_loja/admin.py
from django.contrib import admin
from .models import Store, Product
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "is_store_owner", "created_at")
    search_fields = ("user__username", "phone")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "store", "price", "quantity", "active", "created_at")
    list_filter = ("active", "store")
    search_fields = ("name", "store__name")
