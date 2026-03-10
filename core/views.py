from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory, Product
from .serializers import InventorySerializer

from .models import *
from .serializers import *
from .services import confirm_order

from rest_framework.permissions import IsAdminUser,IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DealerViewSet(viewsets.ModelViewSet):

    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["post"])
    def confirm(self, request, pk=None):

        order = self.get_object()

        try:

            confirm_order(order)

            return Response(
                {"message": "Order confirmed successfully"}
            )

        except ValueError as e:

            return Response(
                {"error": str(e)}
            )

    @action(detail=True, methods=["post"])
    def deliver(self, request, pk=None):

        order = self.get_object()

        if order.status != "confirmed":

            return Response(
                {"error": "Order must be confirmed first"}
            )

        order.status = "delivered"
        order.save()

        return Response(
            {"message": "Order delivered"}
        )
    
class InventoryListView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):

        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)

        return Response(serializer.data)
    
class InventoryUpdateView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, product_id):

        try:
            inventory = Inventory.objects.get(product_id=product_id)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=404)

        quantity = request.data.get("quantity")

        if quantity is None:
            return Response({"error": "Quantity required"}, status=400)

        inventory.quantity = quantity
        inventory.save()

        serializer = InventorySerializer(inventory)

        return Response(serializer.data)