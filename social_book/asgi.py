"""
ASGI config for social_book project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
>>>>>>> 3406665d12657f3e50966f6e0d60891ea0411ce8
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_book.settings')

application = get_asgi_application()
