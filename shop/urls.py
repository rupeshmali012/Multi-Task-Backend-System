from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, get_recommendations

# --- Task 3: API Routing (E-commerce) ---

# 1. Using DefaultRouter to automate URL patterns for Products and Orders.
# This generates standard endpoints like /api/shop/products/ and /api/shop/orders/.
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

# --- Task 4: AI Engine Routing ---

urlpatterns = [
    # Standard CRUD endpoints from the router
    path('', include(router.urls)),
    
    # Custom Endpoint for AI Recommendations:
    # This path takes a product_id (integer) and returns recommended products
    # Path: /api/shop/recommend/<product_id>/
    path('recommend/<int:product_id>/', get_recommendations),
]