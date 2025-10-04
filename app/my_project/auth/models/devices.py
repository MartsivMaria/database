class Devices:
    def __init__(self, device_id, room_id, name, type, status):
        self.device_id = device_id
        self.room_id = room_id
        self.name = name
        self.type = type
        self.status = status


    def  to_dict(self):
        return {
            "device_id": self.device_id,
            "room_id": self.room_id,
            "name": self.name,
            "type": self.type,
            "status": self.status,
        }
 