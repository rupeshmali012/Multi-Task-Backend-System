from rest_framework import serializers
from .models import Product, Order

# --- Task 3: E-commerce Data Serialization ---

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    Exposes all product details (name, price, stock) for the storefront API.
    """
    class Meta:
        model = Product
        # Including all fields to provide complete product information
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    Includes security measures to prevent price and status manipulation by the client.
    """
    class Meta:
        model = Order
        fields = '__all__'
        
        # --- Security & Logic ---
        # These fields should NOT be sent by the user/frontend.
        # 1. total_price: Calculated by the server logic (Price * Quantity).
        # 2. status: Controlled by the admin/system, not the customer.
        # 3. ordered_at: Automatically set by the database.
        read_only_fields = ['total_price', 'status', 'ordered_at']