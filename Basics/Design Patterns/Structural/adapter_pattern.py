"""
Problem statement

Imagine you are building an e-commerce website (like Flipkart or Amazon) that sends email notifications to customers (order confirmations, shipping updates, etc).

Right now, you are using your own custom email system called EmailNotificationService. Everything works fine!

But now you want to switch to a popular third-party email service like SendGrid (which is faster, more reliable and handles spam better). 

The problem: your existing code expects one interface but sendgrid has a completely different interface. They don't match!
"""

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass

class EmailNotificationService(NotificationService):
    def send(self, to, title, body):
        print("Sending Email through EmailNotificationService")
        print(f"To = {to}")
        print(f"Title = {title}")
        print(f"body = {body}")

class SendGridEmailService:
    def send_email(self, recipient: str, subject: str, content: str):
        print("Sending Email through SendGridEmailService")
        print(f"recipient = {recipient}")
        print(f"subject = {subject}")
        print(f"content = {content}")

class SendGridAdapter(NotificationService):
    def __init__(self, send_grid_service: SendGridEmailService):
        self.__send_grid_service = send_grid_service

    def send(self, to: str, title: str, body: str):
        self.__send_grid_service.send_email(to,title,body)
class OrderService:
    def __init__(self,email_service: NotificationService):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send("info@abc.com", "New order", "Order has been placed")

# email_notification_service = EmailNotificationService()
# order_service = OrderService(email_notification_service)
# order_service.create_order()

# can't achieve below
# send_grid_service = SendGridEmailService()
# order_service = OrderService(send_grid_service)
# order_service.create_order()


send_grid_service = SendGridEmailService()
send_grid_adapter = SendGridAdapter(send_grid_service)
order_service = OrderService(send_grid_adapter)
order_service.create_order()