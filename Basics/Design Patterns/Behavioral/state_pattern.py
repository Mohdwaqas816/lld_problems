"""
Problem Statement

Imagine you are creating a DirectionService class for a maps applications like Google Maps. This service need to calculate how long (ETA) it will take to reach your destination and what route (directions) to follow between two locations. The travel time and route change depending on your chosen mode of transport.
 - Walking
 - Cycling
 - Car
 - Train
"""

############ BAD CODE #############
# from enum import Enum

# class TransportMode(Enum):
#     WALKING = 'walking'
#     BIKE = 'bike'
#     TRAIN = 'train'

# class TransportService:
#     def __init__(self,transport_mode:TransportMode):
#         self.__transport_mode = transport_mode

#     def set_mode(self,new_transport_mode:TransportMode):
#         self.__transport_mode = new_transport_mode

#     def eta(self):
#         if self.__transport_mode == TransportMode.WALKING:
#             print("Walking will take 15 mins")
#         elif self.__transport_mode == TransportMode.BIKE:
#             print("bike will take 10 mins")
#         elif self.__transport_mode == TransportMode.TRAIN:
#             print("train will take 5 mins")

#     def directions(self):
#         if self.__transport_mode == TransportMode.WALKING:
#             print("Go straight and take left")
#         elif self.__transport_mode == TransportMode.BIKE:
#             print("bike will take 10 mins")
#         elif self.__transport_mode == TransportMode.TRAIN:
#             print("train will take 5 mins")


# transport_service = TransportService(TransportMode.WALKING)
# transport_service.eta()
# transport_service.directions()


"""
Problem in above code

1 - Messy if-else chains and tight dependencies
    - The DirectionService class relies heavily on if-else statements to check which transportation mode is active and then calculate travel time and routes accordingly.
    - when you keep adding more transportation options, these conditional checks grow longer and more complicated, making the code difficult to read and update.

2 - Breaking the open/closed principle
    - Introducing a new transportation mode (like Airplane or Boat) means you have to go back and modify the DirectionService class itself, which violates the open/closed principle (code should be open for adding features but closed for changing existing code)
"""

########## GOOD CODE ############

from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def directions(self):
        pass


class BikeMode(TransportMode):
    def eta(self):
        print("Bike will take 15 mins")

    def directions(self):
        print("Go left to the road")
    
class TrainMode(TransportMode):
    def eta(self):
        print("Train will take 5 mins")

    def directions(self):
        print("Take left and then right")

class TransportService:
    def __init__(self,mode:TransportMode):
        self.__mode = mode

    def set_mode(self,new_mode:TransportMode):
        self__mode = new_mode

    def eta(self):
        self.__mode.eta()

    def directions(self):
        self.__mode.directions()


bike_mode = BikeMode()
train_mode = TrainMode()
transport_service = TransportService(bike_mode)
transport_service.eta()
transport_service.directions()



"""
State pattern structure


Context: This is the main class (like DirectionService) that keeps track of which state is currently active.

State: This is the interface that defines what methods all states must have (like calculating ETA or getting directions).

Concrete State: These are the actual state classes (like WalkingMode, CarMode, TrainMode) that implement the state interface. Each one represents a different mode or conditions of the context object.

"""

"""
Examples : 

Music Player : A music player app that behaves differently depending on its current state (playing, paused or stopped). The play button does different things in each state

Order Tracking system: An e-commerce order that moves through different states like Order Placed, Packing, Shipped, Out for Delivery, and Delivered. Each state has different actions available.

ATM Machine: An ATM that changes behavior based on its state (idle, card inserted, PIN verification, selecting transaction, dispensing cash). Each state allows different options

Traffic Light System: A traffic signal that cycles through states (green, yellow, green) where each state determines what vehicles can do and automatically transitions to the next state after a timer.

"""
