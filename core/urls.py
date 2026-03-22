from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Task 1 & 2 ke liye (Purana rasta thoda update kiya hai clarity ke liye)
    path('api/blog/', include('blog.urls')),
    
    # Task 3 ke liye (Naya rasta)
    path('api/shop/', include('shop.urls')),
]