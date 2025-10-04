from flask import Blueprint, request, jsonify
from ..services.notification_settings_service import NotificationSettingsService

def create_notification_settings_controller(mysql):
    notification_settings_controller = Blueprint('notification_settings', __name__)
    service = NotificationSettingsService(mysql)

    @notification_settings_controller.route('/notificationsettings', methods=['GET'])
    def get_notification_settings():
        try:
            settings = service.get_notification_settings()
            return jsonify([setting.to_dict() for setting in settings])
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @notification_settings_controller.route('/notificationsettings/<int:setting_id>', methods=['DELETE'])
    def delete_notification_settings(setting_id):
        try:
            service.remove_notification_settings(setting_id)
            return jsonify({"message": "Notification setting deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    @notification_settings_controller.route('/notificationsettings/threshold', methods=['GET'])
    def get_notification_threshold():
        operation = request.args.get('operation')
        
        # Перевірка, чи правильно вказано операцію
        if operation not in ['MAX', 'MIN', 'SUM', 'AVG']:
            return jsonify({"error": "Invalid operation type. Use MAX, MIN, SUM, or AVG."}), 400
        
        try:
            result = service.get_threshold(operation)
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return notification_settings_controller

