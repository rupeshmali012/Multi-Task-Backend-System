from django.contrib import admin
from django.urls import path, include

# This is the Root URL configuration for the entire Backend System.
# It acts as a router that directs incoming traffic to specific application modules.

urlpatterns = [
    # 1. Django Admin Panel: Internal dashboard for managing database records
    path("admin/", admin.site.urls),
    
    # 2. Blog & Chat Module (Task 1 & Task 2):
    # All requests starting with 'api/blog/' are handled by the 'blog' application.
    path('api/blog/', include('blog.urls')),
    
    # 3. E-commerce & AI Module (Task 3 & Task 4):
    # All requests starting with 'api/shop/' are handled by the 'shop' application.
    path('api/shop/', include('shop.urls')),
]