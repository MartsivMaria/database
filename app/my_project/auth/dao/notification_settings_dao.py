from ..models.notification_settings import NotificationSettings

class NotificationSettingsDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_notification_settings(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM notificationsettings")
        settings = cur.fetchall()
        cur.close()
        return [NotificationSettings(id=row[0], user_id=row[1], notification_type=row[2], treshold=row[3]) for row in settings]


    def delete_notification_settings(self, id):
        # Тут логіка для заборони видалення (потрібно обробити на рівні сервісу)
        raise Exception("Deleting rows from notificationsettings table is not allowed")

    def calculate_threshold(self, operation):
        cur = self.mysql.connection.cursor()
        
        # Викликаємо збережену функцію
        cur.execute("SELECT calculate_notification_threshold(%s)", (operation,))
        result = cur.fetchone()[0]  # Отримуємо результат функції

        cur.close()

        return result
