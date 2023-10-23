import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from info.consumers import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sysinfo.settings')

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/system_info/', TestConsumer.as_asgi()),
    ]),
})
