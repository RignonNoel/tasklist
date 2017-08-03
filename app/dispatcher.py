import json
from django.core import serializers

class Dispatcher():
    socket = None

    def __init__(self, socket):
        self.socket = socket

    def notify(self, notification):
        self.socket.emit({
            'id': notification.id,
            'receiver_id': notification.receiver_id,
            'sender_id': notification.sender_id,
            'title': notification.title,
            'text': notification.text,
            'published_date': notification.published_date.strftime('%Y-%m-%d %H:%M'),
            'status': notification.status,
            'target_type': notification.target_type,
            'target_id': notification.target_id,
            'target_intention': notification.target_intention
        })
        return self



