from django.apps import AppConfig

# This class handles the configuration and metadata for the 'shop' application.
# The 'shop' app is responsible for Task 3 (E-commerce) and Task 4 (AI Recommendations).
class ShopConfig(AppConfig):
    # Setting the default type for primary key (ID) fields to BigAutoField (Django 3.2+ standard)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the application as registered in core/settings.py
    name = "shop"