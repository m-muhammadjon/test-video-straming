import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import stream.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            stream.routing.websocket_urlpatterns
        )
    ),
})
