"""
When creating an object that needs many different settings - especially when most of them are optional - the constructor becomes messy and confusing.

This creates several problems: 
1 - Extremely long parameter lists in the constructor
2 - Hard to remember which parameters are required and which are optional
3 - No flexibility to set only specific values you need
"""

########### BAD EXAMPLE ##############

# class Laptop:
#     def __init__(self,processor:str, ram:str, graphic_card:str = None, color:str = None, screen_size:str = None):
#         self.processor = processor
#         self.ram = ram
#         self.graphic_card = graphic_card
#         self.color = color
#         self.screen_size = screen_size

#     def display_specs(self):
#         print(f"Processor = {self.processor}")
#         print(f"RAM = {self.ram}GB")
#         if self.graphic_card:
#             print(f"Graphic car = {self.graphic_card}")
#         if self.color:
#             print(f"Color = {self.color}")
#         if self.screen_size:
#             print(f"Screen size = {self.screen_size}")

# laptop1 = Laptop("i5","6")
# laptop1.display_specs()

# laptop2 = Laptop("i5-3232","6",None,"Black","22 inches") # it becomes hard to identify which parameters are for which and what they are
# laptop2.display_specs()


############# GOOD EXAMPLE ############

class Laptop:
    processor = None
    ram = None
    graphic_card = None
    color = None
    screen_size = None

    def display_specs(self):
        if self.processor:
            print(f"processor = {self.processor}")
        if self.ram:
            print(f"ram = {self.ram}")
        if self.graphic_card:
            print(f"Graphic card = {self.graphic_card}")
        if self.color:
            print(f"Color = {self.color}")
        if self.screen_size:
            print(f"Screen size = {self.screen_size}")



class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()

    def set_processor(self,processor:str):
        self.__laptop.processor = processor
        return self
    
    def set_ram(self,ram:str):
        self.__laptop.ram = ram
        return self 
    
    def set_graphic_card(self,set_graphic_card:str):
        self.__laptop.graphic_card = set_graphic_card
        return self 
    
    def set_color(self,color:str):
        self.__laptop.color = color
        return self 
    
    def set_screen_size(self,screen_size:str):
        self.__laptop.screen_size = screen_size
        return self 

    def build(self):
        return self.__laptop

    
# the below line is called method chaining
l = LaptopBuilder().set_processor("i5-4323").set_ram("i5").build()
l.display_specs()

