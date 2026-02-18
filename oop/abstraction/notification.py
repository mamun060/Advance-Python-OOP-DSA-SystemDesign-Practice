from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass 

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification with message: {message}")


def notify_user(notification: Notification, message: str):
    notification.send(message)

notify_user(EmailNotification(), "Hello via Email!")
notify_user(SMSNotification(), "Hello via SMS!")
notify_user(PushNotification(), "Hello via Push Notification!")
notify_user(PushNotification(), "Hello via Push Notification!")

