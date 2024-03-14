class User:
    def __init__(self,user_id:int,username:str):
        self.books = []
        self.user_id = user_id
        self.username = username
    def into(self):
        return ', '.join(sorted((self.books),reverse=False)

    def __str__(self):
        rentedbooks = ', '.join(self.books)
        return f'{self.user_id}, {self.username}, {rentedbooks}'