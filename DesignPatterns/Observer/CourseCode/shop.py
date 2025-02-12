from DesignPatterns.Observer.CourseCode.decorator import notify_observers
from DesignPatterns.Observer.CourseCode.notification import EmailNotification, SMSNotification, PushNotification


class Product:
    pass


class Payment:
    observers = [
        SMSNotification,
        PushNotification,
    ]

    @notify_observers(message='purchase paid')
    def checkout(self):
        pass


class Purchase:
    observers = [
        EmailNotification,
        SMSNotification,
        PushNotification,
    ]

    def __init__(self, product_list):
        self.product_list = product_list
        self.payment = Payment()

    def checkout(self):
        self.payment.checkout()

    @notify_observers(message='purchase cancel')
    def cancel(self):
        pass
