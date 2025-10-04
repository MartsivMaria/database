from flask import Blueprint, request, jsonify
from services.devices_service import DevicesService

def create_devices_controller(mysql):
    devices_controller = Blueprint('devices', __name__)
    service = DevicesService(mysql)

    @devices_controller.route('/devices', methods=['GET'])
    def get_devices():
        try:
            devices = service.get_devices()
            return jsonify([device.to_dict() for device in devices]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @devices_controller.route('/devices', methods=['POST'])
    def create_device():
        data = request.json
        if not data or 'device_id' not in data or 'room_id' not in data or 'name' not in data or 'type' not in data or 'status' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_device(data)
            return jsonify({"message": "Device created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @devices_controller.route('/devices/<int:device_id>', methods=['PUT'])
    def update_device(device_id):
        data = request.json
        if not data or 'room_id' not in data or 'name' not in data or 'type' not in data or 'status' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_device(device_id, data)
            return jsonify({"message": "Device updated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @devices_controller.route('/devices/<int:device_id>', methods=['DELETE'])
    def delete_device(device_id):
        try:
            service.remove_device(device_id)
            return jsonify({"message": "Device deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return devices_controller
