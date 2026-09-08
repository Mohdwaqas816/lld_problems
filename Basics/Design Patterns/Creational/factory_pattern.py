"""
Problem Statement

Imagine you are building a food ordering app where customers can order different types of meals (Pizza, Burger, Pasta). Initially you might create separate classes for each food type and create objects like this.

pizza = Pizza()
burger = Burger()
pasta = Pasta()

But as your restaurant grows and you keep adding new menu items (Biryani, Dosa, Momos, Chinese, etc.), directly creating these objects in your code becomes messy and hard to manage, especially when the creation logic gets more complex.

"""

########## BAD EXAMPLE ##########
# from abc import ABC, abstractmethod

# class Food(ABC):
#     @abstractmethod
#     def prepare(self):
#         pass


# class Pizza:
#     def prepare(self):
#         print("preparing pizza")

# class Burger:
#     def prepare(self):
#         print("preparing burger")

# class RestaurantService:
#     def create_order(self,food_type:str):
#         if food_type == "pizza":
#             f = Pizza()
#         elif food_type == 'burger':
#             f = Burger()
#         else:
#             print("Invalid food type")
#             return None
#         f.prepare()
#         return f

# restaurant_service = RestaurantService()
# restaurant_service.create_order('pizza')

"""
Problems

1 - The client code (RestaurantService) is tightly connected to specific classes (Pizza, Burger,Pasta), making it dependent on knowing about each food type.

2 - Adding new food items means you have to go back and modify the RestaurantService code, breaking the Open/Closed Principle.


Solution 

The Factory patterns moves all object creation logic into one central place - the factory class. Instead of creating objects directly throughout your code, you hand over this responsibility to the factory, which decides which specific class to create based on the request. This approach follows the Open/Closed principle by allowing you to add new food types without changing any existing code - you only update the factory.


1 - Factory Class: The FoodFactory class holds all the logic for creating different food items based on what the customer orders. This keeps all creation logic in one place, making it simple to add or modify food types.

2 - Decoupling: The RestaurantService class (Client) no longer needs to know how pizza, burger or pasta objects are created. It simply asks the factory to create the food item and receives it ready to use.

3 - Flexibility: Adding a new food type (like biryani) only means updating the factory - the RestaurantService code stays completely unchanged

"""

from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza:
    def prepare(self):
        print("preparing pizza")

class Burger:
    def prepare(self):
        print("preparing burger")

class FoodFactory:
    @staticmethod
    def create_food(food_type:str) -> Food:
        if food_type == 'pizza':
            return Pizza()
        elif food_type == 'burger':
            return Burger()
        else:
            return None

class RestaurantService:
    def create_order(self,food_type:str):
        food = FoodFactory.create_food(food_type)
        if food is None:
            print("Can't prepare food")
            return None
        food.prepare()
        return food
     

restaurant_service = RestaurantService()
restaurant_service.create_order("pizza")        
restaurant_service.create_order("burger")   

"""
Real World Use cases

1 - User Interface libraries: When building apps, the type of button or UI element created depends on which platform you are running on (Windows, macOs, or Linux). A factory decides which platform - specific component to create at runtime

2 - DataBase Connections: When an application needs to connect to different database systems (like MySQL or MongoDB), a factory chooses which databases connector to create based on the configuration settings.

3- File Export Tools: when users want to export documents to different formats (PDF, Word, HTML) a factory determines which file generator to create based on the user's selection.
"""


