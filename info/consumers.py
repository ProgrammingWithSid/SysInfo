from channels.generic.websocket import WebsocketConsumer
import json
from .models import PCSystemInfo
from asgiref.sync import async_to_sync

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))

    def receive(self, text_data=None):
        try:
            data = json.loads(text_data)
            pc_data = data.get(list(data.keys())[0], {}).get("system_info", {})
            pc_name = list(data.keys())[0]
            if pc_data and pc_name:
                pc_data["pc_name"] = pc_name
                pc_obj, created = PCSystemInfo.objects.update_or_create(
                    pc_name=pc_name,
                    defaults=pc_data
                )
                if not created:
                    for key, value in pc_data.items():
                        setattr(pc_obj, key, value)
                    pc_obj.save()
        except json.JSONDecodeError:
            pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.room_group_name
        )
