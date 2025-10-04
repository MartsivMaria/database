from flask import Flask
from flask_mysqldb import MySQL
from .config import Config 
from controller.objects_controller import create_objects_controller
from controller.users_controller import create_users_controller
from controller.notifications_controller import create_notifications_controller
from controller.sensor_notification_controller import create_sensor_notification_controller
from controller.devices_controller import create_devices_controller
from controller.corridors_controller import create_corridors_controller
from controller.notification_settings_controller import create_notification_settings_controller
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

objects_controller = create_objects_controller(mysql)
app.register_blueprint(objects_controller)

users_controller = create_users_controller(mysql)
app.register_blueprint(users_controller)

notifications_controller = create_notifications_controller(mysql)
app.register_blueprint(notifications_controller)

sensor_notification_controller = create_sensor_notification_controller(mysql)
app.register_blueprint(sensor_notification_controller)

devices_controller = create_devices_controller(mysql)
app.register_blueprint(devices_controller)

corridors_controller = create_corridors_controller(mysql)
app.register_blueprint(corridors_controller)

notification_settings_controller = create_notification_settings_controller(mysql)
app.register_blueprint(notification_settings_controller)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)

