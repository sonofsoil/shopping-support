from django.urls import path
from support_app.consumers import QueryWebSocketConsumer

ws_urlpatterns = [
    path('ws/trace/', QueryWebSocketConsumer.as_asgi())
]