from ..models.devices import Devices

class DevicesService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_devices(self):
        query = "SELECT * FROM ajax_systems.devices"
        connection = self.mysql.connection
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        # Конвертуємо результат у список словників
        devices = []
        for row in result:
            devices.append({
                'device_id': row[0],
                'room_id': row[1],
                'name': row[2],
                'type': row[3],
                'status': row[4]
            })
        return devices

    def add_device(self, data):
        query = """
        INSERT INTO ajax_systems.devices (device_id, room_id, name, type, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        connection = self.mysql.connection
        cursor = connection.cursor()
        cursor.execute(query, (data['device_id'], data['room_id'], data['name'], data['type'], data.get('status', 'active')))
        connection.commit()
        cursor.close()

    def modify_device(self, device_id, data):
        query = """
        UPDATE ajax_systems.devices
        SET room_id = %s, name = %s, type = %s, status = %s
        WHERE device_id = %s
        """
        connection = self.mysql.connection
        cursor = connection.cursor()
        cursor.execute(query, (data['room_id'], data['name'], data['type'], data['status'], device_id))
        connection.commit()
        cursor.close()

    def remove_device(self, device_id):
        query = "DELETE FROM ajax_systems.devices WHERE device_id = %s"
        connection = self.mysql.connection
        cursor = connection.cursor()
        cursor.execute(query, (device_id,))
        connection.commit()
        cursor.close()

