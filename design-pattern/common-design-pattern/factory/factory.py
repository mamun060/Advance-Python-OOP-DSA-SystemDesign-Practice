from abc import ABC, abstractmethod

# Base Interface
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


# Concrete Classes
class EmailNotification(Notification):
    def send(self):
        return "Email পাঠানো হয়েছে"


class SMSNotification(Notification):
    def send(self):
        return "SMS পাঠানো হয়েছে"


# Factory Class
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("ভুল notification টাইপ")
