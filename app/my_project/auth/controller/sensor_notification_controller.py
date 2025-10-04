from flask import Blueprint, jsonify, request
from ..services.sensor_notification_service import SensorNotificationService

def create_sensor_notification_controller(mysql):
    sensor_notification_controller = Blueprint('sensor_notification', __name__)
    service = SensorNotificationService(mysql)

    @sensor_notification_controller.route('/sensors_notifications', methods=['GET'])
    def get_sensors_notifications():
        try:
            grouped_data = service.get_all_sensors_notifications()

            return jsonify(grouped_data)  
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    
    @sensor_notification_controller.route('/sensors_notifications', methods=['POST'])
    def add_sensor_notification():
        try:
            data = request.get_json()
            sensor_type = data.get('sensor_type')
            notification_message = data.get('notification_message')

            if not sensor_type or not notification_message:
                return jsonify({"error": "Missing required fields"}), 400

            service.insert_sensor_notification_link(sensor_type, notification_message)
            return jsonify({"message": "Link added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    return sensor_notification_controller
