# library_management_system_V1
Sure! Here’s a clean and simple *`README.md`* for your *Library Management System* project:

---

📚 Library Management System (Python)

A command-line based Library Management System built using *Object-Oriented Programming (OOP)* in Python. This project simulates how a basic library works—allowing you to add books, register users, borrow and return books, and view records.

---

🚀 Features

- Add new books to the library
- Register new library members with unique 8-digit IDs
- Check if a member ID already exists
- Borrow and return books with validation
- Prevent borrowing books that aren’t in the library
- View all available and borrowed books
- Clean user input handling and validation

---

🧠 Concepts Used

- *Object-Oriented Programming*
  - Classes: `Book`, `User`,`library`
  - Objects to represent books and members
- *Functions* to handle core operations
- *Control Flow*: if-else logic for menu selection and input validation
- *Lists and Tuples* for storing book and user data
- *String methods* for case-insensitive searching and formatting

---

📂 Structure
- system.py: Main program logic
- objects.py: Contains class definitions for Book and User
- library_books: A list of tuples with book info (title, author, ISBN)
  
📸 Sample Run

bash
----1.Add new books to the library----
----2.Register new users----
----3.Borrow books----
----4.Return books----
----5.View all available and borrowed books----
What would you like to do? 2
Enter name: alice johnson
Enter user ID (8 digits): 12345678
Has the member borrowed any library books? (y/n): y
Enter the title of the borrowed book: 1984
Member added with borrowed book.


---

✅ To-Do / Future Improvements

- Add file storage (save/load members and books)
- GUI version using Tkinter or web version with Flask
- Book availability status tracking
- Support for multiple borrowed books at once via menu

---

🛠️ Getting Started

1. Clone the repo  
   git clone https://github.com/chunu-siba/library_management_system_V1.git
2. Open it in PyCharm or any code editor
3. Run system.py

---

📃 License

MIT License
This project is licensed under the MIT License - see the LICENSE file for details.
---

- `system.py`: Main program logic
- `objects.py`: Contains class definitions for `Book` and `User`
- `library_books`: A list of tuples with book info (title, author, ISBN)
