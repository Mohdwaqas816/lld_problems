"""
Definition: A class should have only one reason to change, meaning it should do only one job or have only one responsibility.

Simple terms: Dont make one class do everything. Each class should focus on one task only.

Example: A User class should only handle user-related data, while database operations should be handled by separate UserRepository class.

Bad Example: 

User Class
 get_user_info()
 is_adult()
 save_to_database()
 delete_from_database()

Good Example:

User Class
 get_user_info()
 is_adult()

UserRepository Class
 save_to_database()
 delete_from_database()

"""

# GOOD EXAMPLE SNIPPET

class User:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        return self.age > 18

class UserRepository:
    def __init__(self,db,user,password):
        self.db = db
        self.user = user
        self.password = password

    # argument : A user object using type annotation
    def save_to_db(self,user:"User"):
        print(f"{user.name} is getting saved to db")

    def delete_from_db(self,user: "User"):
        print(f"{user.name} is getting deleted from db")

# creating object
user_obj = User("Waqas",30, "abc@xyz.com")
user_repo = UserRepository("userDB","root","root")


# printing and saving object
user_obj.get_user_info()
user_repo.save_to_db(user_obj)



    