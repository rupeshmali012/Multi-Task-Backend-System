"""
WSGI config for core project.
This file is the entry point for synchronous web servers to communicate with your Django project.
Used for traditional HTTP requests (Task 1, 3, and 4).
"""

import os
from django.core.wsgi import get_wsgi_application

# 1. Setting the default Django settings module for the WSGI service
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# 2. This 'application' variable is used by servers like Gunicorn or uWSGI to run the project
application = get_wsgi_application()