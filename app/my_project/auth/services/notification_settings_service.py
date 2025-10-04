from dao.notification_settings_dao import NotificationSettingsDAO

class NotificationSettingsService:
    def __init__(self, mysql):
        self.dao = NotificationSettingsDAO(mysql)

    def get_notification_settings(self):
        return self.dao.get_all_notification_settings()

    def remove_notification_settings(self, id):
        try:
            self.dao.delete_notification_settings(id)
        except Exception as e:
            raise Exception(str(e))

    def get_threshold(self, operation):
        # Викликаємо DAO для отримання результату функції
        return self.dao.calculate_threshold(operation)