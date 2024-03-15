from user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}
    def get_book(self,author:str,book_name:str,days_to_return:int,user:User):
        for eachkey, eachval in self.books_available.items():
            if book_name in eachval:
                eachval.remove(book_name)
                self.rented_books[user][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            else:
                return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'
    def return_book(self,author:str, book_name:str, user: User):
        if book_name in self.rented_books[user]:
            self.rented_books[user].pop(book_name)
            if author not in self.books_available:
                self.books_available[author] = book_name
            else:
                self.books_available[author] += book_name
        else:
            return f"{user} doesn't have this book in his/her records!"

