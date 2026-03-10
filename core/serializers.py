from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    stock = serializers.IntegerField(
        source="inventory.quantity",
        read_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name", read_only=True)
    sku = serializers.CharField(source="product.sku", read_only=True)

    class Meta:
        model = Inventory
        fields = ["id", "product", "product_name", "sku", "quantity", "updated_at"]


class DealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealer
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "unit_price"]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "dealer", "items", "status"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(
            order=order,
            product=item["product"],
            quantity=item["quantity"],
            unit_price=item["unit_price"],
            line_total=item["quantity"] * item["unit_price"]
        )
            return order