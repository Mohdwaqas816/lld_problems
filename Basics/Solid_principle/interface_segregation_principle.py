"""
Definition: The interface Segregation Principle ensures that classes are not force to implement methods they dont need

Simple terms: Break large, general-purpose interfaces into smaller, more specific ones.

Benefits: 
    - Maintainability - Code is easier to maintain and update
    - Flexibility - Classes can pick and choose what they need
    - Testability - Easier to test because classes have only what they need

Key Rule: Classes should only depend on the methods they actually use.

"""

########### BAD EXAMPLE ##############
from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def work(self):
#         pass


# class Worker(Employee):
#     def eat(self):
#         print("Worker is eating")
#     def work(self):
#         print("worker is working")

# class Robot(Employee):
#     def eat(self):
#         raise Exception("Robot can't eat")
#     def work(self):
#         print("robot is working")

# r = Robot()
# r.eat()



####### GOOD EXAMPLE #########

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot is working")

class Employee(Workable,Eatable):
    def work(self):
        print("Employee is eating")
    def eat(self):
        print("Employee is working")

e = Employee()
e.work()
e.eat()