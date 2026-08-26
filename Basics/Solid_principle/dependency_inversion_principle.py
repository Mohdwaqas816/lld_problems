"""
Definition: High level modules (business logic) should not depend directly on low-level modules (specific implementations). Both should depend on abstractions (interfaces).

Simple terms:
    - High-level: Main business logic (what your app does)
    - Low-level: Specific implementations (database,email,etc.)
    - Abstraction: Interface/contract between them
"""



######### BAD EXAMPLE ###########

# class NotificationService:
#     def __init__(self):
#         self.email_service = EmailService()
#         self.sms_service = SMSService()

#     def notify_by_email(self,message):
#         self.email_service.send_email(message)

#     def notify_by_sms(self,message):
#         self.sms_service.send_sms(message)
    
# class EmailService:
#     def send_email(self,message):
#         print(f"sending email- {message}")

# class SMSService:
#     def send_sms(self,message):
#         print(f"sending sms - {message}")


# ns = NotificationService()
# ns.sms_service.send_sms("Sending message")
# ns.email_service.send_email("Sending email")

######### GOOD EXAMPLE #########
from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self,message):
        pass

class EmailService(NotificationChannel):
    def send(self, message):
        print(f"Sending email : {message}")

class SMSService(NotificationChannel):
    def send(self, message):
        print(f"Sending sms : {message}")

class NotificationService:
    def __init__(self,channel: NotificationChannel):
        self.channel = channel

    def notify(self,message):
        self.channel.send(message)


sms_service = SMSService()
ns = NotificationService(sms_service)
ns.notify("Hey")


 