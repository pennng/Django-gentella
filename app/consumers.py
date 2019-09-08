from channels.generic.websocket import AsyncWebsocketConsumer
import json


class LiveConsumer(AsyncWebsocketConsumer):
    groups = ["broadcast"]

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()

    def channel_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))