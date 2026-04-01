import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# 1. Setting the default Django settings module for the ASGI service
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# 2. Manually initializing Django (Required for standalone ASGI/Channels setup)
django.setup()

# Importing the WebSocket routes from the blog application
import blog.routing

# 3. Main ASGI Application entry point
# ProtocolTypeRouter acts as a switchboard to handle different types of requests
application = ProtocolTypeRouter({

    # Handles standard HTTP requests (e.g., Blog API, E-commerce views)
    "http": get_asgi_application(),

    # Handles Real-time WebSocket connections (Task 2: Chat Server)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # Directing traffic to the paths defined in blog/routing.py
            blog.routing.websocket_urlpatterns
        )
    ),
})