from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SellerProductViewSet

router = DefaultRouter()
router.register(r'seller/products', SellerProductViewSet, basename='seller-products')

urlpatterns = [
    path('', include(router.urls)),
]
