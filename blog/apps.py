from django.apps import AppConfig

# This class handles the configuration and metadata for the 'blog' application.
class BlogConfig(AppConfig):
    # Setting the default type for primary key (ID) fields in the database
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the application as recognized by Django's app registry
    name = "blog"