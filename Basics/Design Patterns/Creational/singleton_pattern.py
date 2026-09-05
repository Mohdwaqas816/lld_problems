"""

For certain components like database connections, application logs, or configuration settings, you need to make sure that only one object of the class exists throughout your entire application. If you accidentally create multiple objects, it can cause serious problems:

 - Conflicting Data: When multiple objects represent the same thing (like a database connection), they might end up holding different information, leading to inconsistent behavior across your application.

 - Wasted Resources: Creating multiple instances of resource-intensive classes (like database connections) consumes unnecessary memory and processing power, slowing down your application significantly

"""

######### BAD EXAMPLE ##########

# class Logger:
#     def __init__(self,file_name:str):
#         self.file_name = file_name
#         self.log_count = 0

#     def log(self,text:str):
#         print(f"Logger is logging {text} in {self.file_name}")
#         self.log_count += 1

# log1 = Logger("app1.log")
# log2 = Logger("app2.log")
# log3 = Logger("app3.log")

# # user log
# log1.log("User is logging in")

# # staff log
# log2.log("staff is blocking user")

# # admin 
# log3.log("admin is adding items")


# print(log1.log_count)  # the log count should be 3
# print(log2.log_count)  # the log count should be 3
# print(log3.log_count)  # the log count should be 3


############## GOOD EXAMPLE ############### 

class Logger:

    __instance = None

    def __new__(cls,file_name:str):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file_name
            cls.__instance.log_count = 0
            return cls.__instance
        else:
            return cls.__instance

    def log(self,msg):
        print(f"Logging in {msg} in {self.file_name}")
        self.log_count += 1

    def get_log_count(self):
        return self.log_count


log1 = Logger("app1.log")
log1.log("Hello")

log2 = Logger("app2.log")
log2.log("Good")

log3 = Logger("app3.log")
log3.log("Bye")

print(log1.get_log_count())
print(log2.get_log_count())
print(log3.get_log_count())
