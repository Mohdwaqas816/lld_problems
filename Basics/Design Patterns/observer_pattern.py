"""
Problem Statement

Imagine you have a weather station that measure temperature. There are multiple devices like phones, TVs and displays that need to show this temperature

Without Observer pattern
- The weather station would need to know about every single device and manually update each one when the temperature changes.

This creates a big problem:
 - Weather station is tightly connected to all devices
 - Adding a new device means changing weather station code
 - Removing a device means changing weather station code again
 - Weather station depends on specific device types

Observer Pattern Benefits

Loose Coupling: The main object (like WeatherStation) does not need to know anything about the specific devices. It just sends notifications to whoever is listening, without caring what type of device it is.

Easy to Scale: You can add as many new devices as you want (phones, TVs, smartwatches, etc.) without changing a single line of code in the WeatherStation. Just register the new device and it starts receiving updates automatically.

Flexible at Runtime: Devices can join or leave the notification list anytime while the program is running. A device can start listening when it needs updates and stop listening when it doesn't.

########## Use cases ############

1 - Event Listeners in Apps: when you build apps with buttons and forms, the observer pattern helps handle user actions. For example, when someone clicks a button or types in a text box, all the listeners get notified automatically and can react accordingly.

2 - Stock Price Tracking: Imagine you are tracking Reliance or TCS stock prices. When the price changes, all investors and trading systems that are watching that stock get instant notifications about the new price. They don't need to keep checking manually.

3 - News apps and blogs: when a news website published a new article, all users who have subscribed to that website automatically receive notifications. Like how you get alerts when your favorite blog posts something new.

4 - Social Media updates: Think of instagram or twitter. When someone you follow posts a new photo or tweet, you get a notification. You are an observer, and the account you follow is the subject. When they post (subject changes), all followers (observers) are notified

"""

######### Wrong Code #########

# class PhoneDisplay:
#     def update(self,temp):
#         print(f"Phone display temperature = {temp}")

# class TVDisplay:
#     def update(self,temp):
#         print(f"TV display temperature = {temp}")

# class WeatherStation:
#     def __init__(self):
#         self.__temperature = 0
#         self.__phone_display = PhoneDisplay()
#         self.__tv_display = TVDisplay()

#     def update_temperature(self,new_temp):
#         self.__temperature = new_temp
#         self.notify_display()

#     def notify_display(self):
#         self.__phone_display.update(self.__temperature)
#         self.__tv_display.update(self.__temperature)

# weather = WeatherStation()
# weather.update_temperature(30)

## Whenever I need to add new display I need to change the Weather station code as well
## hence the above code is tightly coupled


############# GOOD CODE ###############
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self,temp):
        pass

class TVDisplay(Observer):
    def update(self, temp):
        print(f"TV temperature updated to {temp}")

class MobileDisplay(Observer):
    def update(self, temp):
        print(f"Mobile temperature updated to {temp}")


class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers: List[Observer] = []

    def add_observer(self, new_observer: Observer):
        self.__observers.append(new_observer)

    def remove_observer(self,ob:Observer):
        self.__observers.remove(ob)

    def update_temperature(self,new_temp):
        self.__temperature = new_temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperature)

ws = WeatherStation()
tv = TVDisplay()
mobile = MobileDisplay()

ws.add_observer(tv)
ws.add_observer(mobile)

ws.update_temperature(30)

