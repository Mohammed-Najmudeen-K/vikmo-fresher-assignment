from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import InventoryListView, InventoryUpdateView
router = DefaultRouter()

router.register("products", ProductViewSet)
router.register("dealers", DealerViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("inventory/", InventoryListView.as_view()),
    path("inventory/<int:product_id>/", InventoryUpdateView.as_view()),
]