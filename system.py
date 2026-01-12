from objects import *
import time
#creating a library management system
# 1. Add new books to the library
# 2. Register new users
# 3. Borrow books
# 4. Return books
# 5. View all available and borrowed books
print('----1.Add new books to the library----')
print('----2.Register new users----')
print('----3.Borrow books----')
print('----4.Return books----')
print('----5.View all available and borrowed books----')
action_input=input('What would you like to do?')
library_books = [
    ("to kill a mockingbird", "harper lee", "9780061120084"),
    ("1984", "george orwell", "9780451524935"),
    ("the great gatsby", "f. scott fitzgerald", "9780743273565"),
    ("pride and prejudice", "jane austen", "9781503290563"),
    ("the catcher in the rye", "j.d. salinger", "9780316769488"),
    ("the hobbit", "j.r.r. tolkien", "9780547928227"),
    ("moby dick", "herman melville", "9781503280786"),
    ("war and peace", "leo tolstoy", "9781853260629"),
    ("the alchemist", "paulo coelho", "9780061122415"),
    ("the book thief", "markus zu's'ak", "9780375842207")
]
library_members = [
    ("alice johnson", "73849201", []),
    ("bob smith", "51928476", [("1984", "george orwell", "9780451524935")
    ]),
    ("charlie davis", "60418293", [("the catcher in the rye", "j.d. salinger", "9780316769488"),
        ("the hobbit", "j.r.r. tolkien", "9780547928227")
    ]),
    ("diana evans", "18273645", [])
]

borrowed_books=[]
returned_books=[]
Library_info=Library(list_of_books=library_books,list_of_users=library_members)
#functions
def add_new_book ():
    print('Proceeding to add a new book')
    title_input=input('Title:')
    author_input=input('Author:')
    isbn_input=input('Isbn:')
    book=Book(title=title_input,author=author_input,isbn=isbn_input)
    print(f"{book.title} has been added successfully!✅")
    book_info=(title_input,author_input,isbn_input)
    library_books.append(book_info)
    print(library_books)

def add_new_member():
    print('proceeding to add a new member')
    name_input=input('please Include both first and last name:')
    if all(part.isalpha() for part in name_input.split()) and len(name_input.strip())>=2:
        user_id_input=input('Members ID:')
        if len(user_id_input) >8 or len(user_id_input) < 8:
            print('Member Id should be 8 characters long')
        else:
            if any( user_id_input ==member_id[1] for member_id in library_members):
                print(f'{user_id_input} already exists please enter an authentic Identity Number')
            else:
                borrowed_books_query=input('has the Member borrowed any library books?(y=yes/n=no:').lower().strip()
                if borrowed_books_query =='y':
                    book_title=input('Enter the title of the borrowed book:')
                    find_book= any(book[0]==book_title for book in library_books)
                    if find_book:
                        print(book_title)
                    else:
                        print('How can one borrow a book that does not exist🤔')
                elif borrowed_books_query =='n':
                    member1=User(name=name_input,user_id=user_id_input,borrowed_books='None')
                    print(member1.name)
                    member_info=(member1.name,member1.user_id,['None'])
                    library_members.append(member_info)
                    print(library_members)
                else:
                    print('invalid input')
    else:
        print('name can not include numbers')
def borrow_books():
    print('----proceeding to borrow a book/s----')
    member_id_verification=input('please enter member Id to be able to borrow books:')
    verification=any(library_member[1] == member_id_verification for library_member in library_members)
    if verification:
        print(f'member can borrow books from this library')
        borrow_book=input('Enter title of book you want borrowed').lower()
        find_book=any(book[0]==borrow_book for book in library_books)
        if find_book:
            print('book available for borrowing')
            confirmation=input('Proceed to borrowing:(y=yes/n=no)?').lower()
            if confirmation=='y':
                for book in library_books:
                        if borrow_book==book[0] :
                            time.sleep(3)
                            print('----------Book Information:----------')
                            print(f"Title: {book[0]}")
                            print(f"Author: {book[1]}")
                            print(f"ISBN: {book[2]}")
                            borrowed_books_info=(
                                book[0],book[1],book[2]
                            )
                            borrowed_books.append(borrowed_books_info)
                            library_books.remove(book)
                            time.sleep(2)
                            print("--------Database change Notice-------")
                            print(f"{book}  has been removed from library books and has been placed in the borrowed books list")
                #Adding the borrowed books information to the members information
                for member in library_members:
                    if member_id_verification == member[1]:
                        member[2].append(borrowed_books)
                        time.sleep(2)
                        print('---------Updating members status----------')
                        print(member)
                        print('Borrowing information has been added successfully to the members history and database')
                    break
            elif confirmation =='n':
                print('Please do not ever waste my time')
            else:
                print('InvalidInput🤬')
        else:
            print(f"{borrow_book} is  not available in the library database")
    else:
        print('Member not registered in the library database to proceed please register member first')
        add_new_member()
def return_books():
    member_id=input('Member ID:')
    book_title=input('Book Title:')
    book_status=input('book Return status:')
    for user_info in library_members:
        for borrowed_books_check in user_info[2]:
            if borrowed_books_check == book_title:
                print("Proceeding to return Books")
                returned_books_info=(member_id,book_title,book_status)
                returned_books.append(returned_books_info)
                time.sleep(3)
                print('------Returned Books-------')
                print(returned_books)
            else:
                time.sleep(3)
                print(f'{member_id} has never borrowed {book_title} so can not return it')
                query=input('would you like to enter the book into the library system(y=yes/n==no)').lower()
                if query=='y':
                    add_new_book()
                else:
                    print('Bye!🫱🏼‍🫲🏼🫱🏼‍🫲🏼🫱🏼')


def return_list_of_books_members():
    library_database=Library(list_of_books=library_books,list_of_users=library_members)
    print("-----List Of Library Members------")
    library_database.users()
    print("-----List of Library Books------")
    library_database.books()
#conditional loops

if action_input=='1':
    for i in range (10):
        print('Enter the book info')
        add_new_book()
elif action_input=='2':
    add_new_member()
elif action_input=='3':
    borrow_books()
elif action_input=='4':
    return_books()
elif action_input =='5':
    return_list_of_books_members()
else:
    print('invalid input😤🤬')