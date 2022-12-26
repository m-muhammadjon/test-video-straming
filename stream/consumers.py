import json

from channels.generic.websocket import AsyncWebsocketConsumer


class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('-----------------')
        print(self.scope['url_route']['kwargs'])
        print('-----------------')
        self.room_name = self.scope['url_route']['kwargs']['uid']
        self.room_group_name = 'video_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'video_stream',
                'text': text_data_json
            }
        )

    # Receive message from room group
    async def video_stream(self, event):
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'text': event
        }))
