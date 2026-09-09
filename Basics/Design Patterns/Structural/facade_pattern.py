"""
The problem: Too many services to talk to

A common real-world example of the Facade patterns is an API Gateway in a microservices system.

Problem Without Facade:
Imagine you are building an e-commerce app (Like Flipkart or Amazon). Your backend is split into multiple separate services:
 - User Service - handles login, profile,etc
 - Order Service - handles placing orders
 - Inventory Service - tracks product stock
 - Payment Service - processes payments

Without a Facade (API Gateway), your mobile app or website would need to directly talk to ALL these services separately

This creates problems:
 - Complex client code: Your app needs to know about all 4 services and their different api's
 - Tight coupling: If you change a service api, you must update the mobile app
 - Exposed Internals: The app knows too much about your backend structure
 - Multiple Network Calls: Slower performance with many API calls
"""

############# BAD EXAMPLE #############

# class UserService:
#     def login(self, username: str, password: str) -> dict:
#         print(f"[UserService] Logging in: {username}")
#         return {"user_id": "UID123", "name": username}

#     def get_profiles(self,user_id:str)-> dict:
#         print(f"[UserService] Getting profile for {user_id}")
#         return {"user_id": user_id, "name": "Rahul", "address": "Mumbai"}

# class OrderService:
#     def get_orders(self,user_id: str) -> list:
#         print(f"[OrderService] Getting orders for: {user_id}")
#         return [
#             {"order_id": "ORD-1", "total": 1500},
#             {"order_id": "ORD-2", "total": 3000}
#         ]


# user_service = UserService()
# order_service = OrderService()


# user_service.login("waqas", "testpass")
# user_service.get_profiles("hjk1233")

# print(order_service.get_orders("hjk1233"))


################# GOOD EXAMPLE ##############

class UserService:
    def login(self, username: str, password: str) -> dict:
        print(f"[UserService] Logging in: {username}")
        return {"user_id": "UID123", "name": username}

    def get_profiles(self,user_id:str)-> dict:
        print(f"[UserService] Getting profile for {user_id}")
        return {"user_id": user_id, "name": "Rahul", "address": "Mumbai"}

class OrderService:
    def get_orders(self,user_id: str) -> list:
        print(f"[OrderService] Getting orders for: {user_id}")
        return [
            {"order_id": "ORD-1", "total": 1500},
            {"order_id": "ORD-2", "total": 3000}
        ]

class APIGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()

    def login_user(self,username:str, password:str):
        return self.__user_service.login(username,password)

    def get_user_profile(self,user_id):
        return self.__user_service.get_profiles(user_id)

    def get_order_details(self,user_id):
        return self.__order_service.get_orders(user_id)

api_gateway = APIGateway() 
res = api_gateway.login_user('test','123')
print(res)