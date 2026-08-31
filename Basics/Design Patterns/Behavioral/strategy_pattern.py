"""
------------ Problem Statement ------------

Imagine you are building an app like Flipkart or Amazon

Customers can get different types of discounts:
 - Diwali sale - 20% off on everything
 - Student Discount - 15% off with college ID
 - First Order - $100 flat discount

Without Strategy Pattern

Every time a new discount comes, you have to modify this function,
Too many if-else statements make code messy.
Hard to test each discount type separately
Violates Open/Closed Principle (we learned in SOLID!)

Problems in code

Issue with if-else Approach

- Too many responsibility: DiscountService class is doing two jobs, deciding which discount to apply and calculating discount. It should only do one job (violates single responsibility principle)
- Hard to Extend: Every time you want to add a new discount type (Like republic day sale, holi offer, monsoon sale), you have to open the DiscountService class and add more if-else statements. This means changing existing working code
- Messy Code: As you keep adding more discount types, the if-else chain becomes longer and longer, making the code harder to read, understand and maintain

"""

################# BAD CODE ##################

# class DiscountService:
#     def calculate_discount(self,discount_type:str):
#         if discount_type == 'Diwali':
#             print("Applying diwali discount of 20%")
#         elif discount_type == 'First_Order':
#             print("Applying first order discount of 10%")
#         else:
#             print("No discount applied")

# discount_service = DiscountService()
# discount_service.calculate_discount("Diwali")
# discount_service.calculate_discount("second_order")


########### GOOD CODE #############

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

class DiwaliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying diwali discount of 20%")

class HoliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying Holi discount of 10%")

class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.__strategy = discount_strategy

    def set_strategy(self,new_discount_strategy: DiscountStrategy):
        self.__strategy = new_discount_strategy

    def process(self):
        self.__strategy.calculate_discount()


holi_discount = HoliStrategy()
diwali_discount = DiwaliStrategy()
discount_service = DiscountService(diwali_discount)
discount_service.process()
discount_service = DiscountService(holi_discount)
discount_service.process()

