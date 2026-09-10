"""
Design Library Book Class
Problem: Create a Book class for a library management system.

Requirements:

Fields: title, author, isbn, isAvailable
Constructor that initializes all fields (book starts as available)
borrowBook(): marks book as unavailable if currently available, returns success/failure
returnBook(): marks book as available
displayInfo(): prints book details including availability status

"""

from typing import List

class Book:
    def __init__(self,title: str, author: str, isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        
    def borrow_book(self):
        if self.is_available:
            self.is_available = False 
            return True 
        else:
            return False
    
    def return_book(self):
        self.is_available = True
    
    def display_info(self):
        status = 'Available' if self.is_available else 'Borrowed'
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status})")


if __name__ == "__main__":
    book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success)}")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success)}")

    book.return_book()
    book.display_info()


