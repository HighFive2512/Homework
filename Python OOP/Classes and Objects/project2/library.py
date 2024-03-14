from user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}
    def get_book(self,author:str,book_name:str,days_to_return:int,user:User):
        if book_name in self.books_available.values():
            self.books_available.pop()