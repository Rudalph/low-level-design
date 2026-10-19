from abc import ABC, abstractmethod

class Notifications(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass
    
class EmailNotification(Notifications):
    def send_notification(self, message):
        print(f"Email Notification: {message}")
        
class SMSNotification(Notifications):
    def send_notification(self, message):
        print(f"SMS Notification: {message}")
        
class PhoneNotification(Notifications):
    def send_notification(self, message):
        print(f"Phone Notification: {message}")
        
class NotificationService:
    def send(self, notification_type, message):
        notification_type.send_notification(message)
        
email = EmailNotification()
sms = SMSNotification()
phone = PhoneNotification()

service = NotificationService()
service.send(email, "Send a neew Email")
    