import json
from channels.generic.websocket import AsyncWebsocketConsumer

# This class handles Real-time Chat logic using WebSockets (Task 2)
# Using 'Async' allows the server to handle multiple chat connections efficiently without blocking.
class ChatConsumer(AsyncWebsocketConsumer):
    
    # 1. Triggered when a user tries to connect to the Chat
    async def connect(self):
        # Extracting the room name from the URL (defined in routing.py)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Creating a unique group name for this specific chat room
        self.room_group_name = f'chat_{self.room_name}'

        # Joining the room group: This allows broadcasting messages to everyone in this room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        # Accepting the WebSocket connection
        await self.accept()

    # 2. Triggered when the user closes the chat tab or disconnects
    async def disconnect(self, close_code):
        # Leaving the room group to stop receiving messages
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # 3. Triggered when a user sends a message from their browser
    async def receive(self, text_data):
        # Parsing the incoming JSON data
        data = json.loads(text_data)
        message = data['message']

        # Broadcasting the message to the entire group (all users in the room)
        # It triggers the 'chat_message' method for every user in the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message', # This calls the chat_message function below
                'message': message
            }
        )

    # 4. This method is called for each user in the group when a message is broadcasted
    async def chat_message(self, event):
        message = event['message']
        
        # Sending the message back to the individual browser via WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
        