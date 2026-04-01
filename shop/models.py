from django.db import models
from django.contrib.auth.models import User

# --- Task 3: E-commerce Product Inventory ---

class Product(models.Model):
    """
    Model representing items available for sale in the shop.
    Also used as the dataset for Task 4 (AI Recommendations).
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # Using DecimalField for precision in monetary values
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Inventory tracking field
    stock = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# --- Task 3: Order Management & User History ---

class Order(models.Model):
    """
    Model representing a purchase transaction made by a user.
    """
    # Defining specific states for an order
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    # Relationship: Linking order to the User who placed it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Relationship: Linking order to the specific Product purchased
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(default=1)
    
    # Storing the final price at the time of purchase
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # State management for the order flow
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"