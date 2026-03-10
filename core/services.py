from django.db import transaction
from .models import Inventory


def confirm_order(order):

    if order.status != "draft":
        raise ValueError("Only draft orders can be confirmed")

    with transaction.atomic():

        for item in order.items.all():

            inventory = Inventory.objects.select_for_update().get(product=item.product)

            if item.quantity > inventory.quantity:
                raise ValueError(
                    f"Insufficient stock for {item.product.name}. "
                    f"Available: {inventory.quantity}, "
                    f"Requested: {item.quantity}"
                )

        for item in order.items.all():

            inventory = Inventory.objects.select_for_update().get(product=item.product)

            inventory.quantity -= item.quantity
            inventory.save()

    order.status = "confirmed"
    order.save()