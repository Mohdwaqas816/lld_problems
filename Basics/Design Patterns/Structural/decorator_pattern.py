"""
You need to add new features or behaviors to an object while your program is running, but creating subclasses for every possible combination would create way too many classes or simplify is not practical

The Problem: Coffee shop ordering system

Imagine you are building a coffee shop ordering system. You start with a basic coffee, but customers want to customize it with different add-ons like Milk, Sugar, Whipped Cream, and Vanilla Syrup- without changing the basic coffee class or creating tons of subclasses for every combination.

Without Decorator Pattern, you would need:
- Coffee
- CoffeeWithMilk
- CoffeeWithSugar
- CoffeeWithWhippedCream
- CoffeeWithMilkAndSugar
- CoffeeWithMilkAndWhippedCream
- CoffeeWithMilkSugarAndWhippedCream
"""

########## BAD EXAMPLE ##########
# from abc import ABC, abstractmethod
# class Beverage(ABC):
#     @abstractmethod
#     def get_description(self):
#         pass

#     @abstractmethod
#     def get_cost(self):
#         pass

# class Coffee(Beverage):
#     def get_description(self):
#         return "Plain Coffee"
#     def get_cost(self):
#         return 20

# class CoffeeWithMilk(Coffee):
#     def get_description(self):
#             return "Coffee with Milk"
#     def get_cost(self):
#         return 30

# coffee1 = Coffee()
# print(coffee1.get_description())
# print(coffee1.get_cost())

# coffee1 = CoffeeWithMilk()
# print(coffee1.get_description())
# print(coffee1.get_cost()) 


######### GOOD EXAMPLE ############

from abc import ABC, abstractmethod
class Beverage(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class Coffee(Beverage):
    def get_description(self):
        return "Plain Coffee"
    def get_cost(self):
        return 20


class AddonDecorator(Beverage):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self):
        pass

    def get_cost(self):
        pass

class MilkDecorator(AddonDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Milk"

    def get_cost(self):
        return self._coffee.get_cost() + 20
    
class WhipCreamDecorator(AddonDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Whip Cream"

    def get_cost(self):
        return self._coffee.get_cost() + 50
    
class SugarDecorator(AddonDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self._coffee.get_cost() + 5


coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = WhipCreamDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

