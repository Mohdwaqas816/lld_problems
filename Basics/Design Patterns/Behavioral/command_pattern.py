"""
Problem Statement

Imagine you are building a restaurant management system. Customers can order different food items like Burger, Pizza and Pasta

Without  Command Pattern, the waiter class would directly call the chef's cooking methods based on what the customer orders.

This creates tight coupling between the waiter and the chef.

The waiter would need to know:
 - what items the chef can cook
 - exactly which methods to call for each item
 - How to handle each specific food type

Three main components:

1 - Command (order) : This is the interface that all food orders must follow. It defines the execute() method that every order type must implement. Think of it as the order slip template - every order slip has the same basic structure.

2 - Invoker (waiter): This is the one who takes the order and passes it to the kitchen. The waiter does not need to know what's in the door. The waiter sends the command.

3 - Receiver (chef) : This is the one who actually does the work. The chef receives the order and performs the cooking operation. The chef performs the actual task.

"""


########## BAD CODE ##########

# class Chef:
#     def cook_pasta(self):
#         print("Chef is cooking Pasta")

#     def cook_pizza(self):
#         print("Chef is cooking Pizza")

# class Waiter:
#     def __init__(self, chef:Chef):
#         self.__chef = chef

#     def place_order(self,item:str):
#         if item == 'Pasta':
#             self.__chef.cook_pasta()
#         elif item == 'Pizza':
#             self.__chef.cook_pizza()
#         else:
#             print("Can't take order")

# chef = Chef()
# waiter = Waiter(chef)
# waiter.place_order('Pizza')

### If chef learn New recipe, we also need to change waiters code


############ GOOD CODE ###############
from abc import ABC, abstractmethod

class Chef:
    def cook_burger(self):
        print("Chef is cooking Burger")

    def cook_pizza(self):
        print("Chef is cooking Pizza")

class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

class PizzaOrder(Order):
    def __init__(self,chef:Chef):
        self.__chef = chef

    def execute(self):
        print("Pizza order")
        self.__chef.cook_pizza()

class BurgerOrder(Order):
    def __init__(self,chef:Chef):
        self.__chef = chef

    def execute(self):
        print("Burger order")
        self.__chef.cook_burger()

class Waiter:
    def take_order(self,order:Order):
        order.execute()


chef = Chef()
burger_order = BurgerOrder(chef)
pizza_order = PizzaOrder(chef)

waiter = Waiter()
waiter.take_order(burger_order)
waiter.take_order(pizza_order)
    
        


