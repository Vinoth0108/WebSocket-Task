# routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/some_path/$', consumers.YourConsumer.as_asgi()),
    re_path(r'D:\Websocket_task', consumers.YourConsumer.as_asgi()),

]
