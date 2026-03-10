from django.contrib import admin
from .models import Product, Dealer, Inventory, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sku", "price", "created_at"]
    search_fields = ["name", "sku"]


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "created_at"]
    search_fields = ["name", "email"]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "updated_at"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "dealer", "status", "total_amount", "created_at"]
    list_filter = ["status"]
    inlines = [OrderItemInline]