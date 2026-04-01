from django.urls import re_path
from . import consumers

# This file defines the WebSocket URL patterns for the 'blog' application.
# It works similarly to urls.py but specifically for real-time bidirectional communication.

websocket_urlpatterns = [
    # Using Regex (re_path) to capture the 'room_name' from the URL.
    # Pattern: ws/chat/ROOM_NAME/
    # Example: ws/chat/msc_students/ will connect to a room named 'msc_students'
    re_path(
        r'ws/chat/(?P<room_name>\w+)/$', 
        consumers.ChatConsumer.as_asgi() # Converting the consumer class to an ASGI app
    ),
]