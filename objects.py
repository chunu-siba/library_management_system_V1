class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    def status(self):
        print('the book is available') if self.is_borrowed == False else print('this book is not available for borrowing')
class User:
    def __init__(self,name,user_id,borrowed_books):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=borrowed_books

class Library:
    def __init__(self,list_of_books,list_of_users):
        self.list_of_books=list_of_books
        self.list_of_users=list_of_users
    def users(self):
        print(self.list_of_users)
    def books(self):
        print(self.list_of_books)
