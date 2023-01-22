from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/comments/", consumers.CommentsConsumer.as_asgi()),
]