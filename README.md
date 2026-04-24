Library Management System
The Library Management System is a lightweight, command-line-based application designed to manage a book collection efficiently. It provides a simple interface to perform core library operations such as adding new titles, viewing the current inventory, and tracking the lending and return process of books.

🚀 Features
Add Books: Easily add new books to the library inventory with their respective author names.

View Inventory: Display a list of all books currently available in the library.

Lend Books: Check out books to borrowers; the system automatically removes the borrowed book from the available inventory.

Return Books: Return books to the library, which updates the collection status.

Simple CLI: Interactive menu-driven interface for seamless navigation.

🛠 How to Run
Prerequisites: Ensure you have Python installed on your system.

Download: Save the LibraryManagementSystem.py file to your local machine.

Execution: Run the script using your terminal or command prompt:

Bash
python LibraryManagementSystem.py
Usage: Follow the on-screen menu prompts to manage your library:

1: Add a book.

2: View available books.

3: Lend a book.

4: Return a book.

0: Exit the application.

📂 Project Logic
The system is built using a library class that utilizes a dictionary to store book titles as keys and their authors as values, ensuring simple and fast lookups for inventory management.
