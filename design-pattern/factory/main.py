from factory import NotificationFactory

notification = NotificationFactory.create_notification("email")
print(notification.send())

notification2 = NotificationFactory.create_notification("sms")
print(notification2.send())
