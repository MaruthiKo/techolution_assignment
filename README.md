# New World Library Management System

Welcome to the **New World Library Management System**!. This system allows you to manage books, users, and book check-in/check-out operations through a command-line interface (CLI).

## Features

- **Book Management:**
  - Add new books.
  - List all books.
  - Update existing books.
  - Delete books.

- **User Management:**
  - Add new users.
  - List all users.
  - Update existing users.
  - Delete users.

- **Check-In/Out Management:**
  - Check out books to users.
  - Return books from users.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logging and Debugging](#logging-and-debugging)
- [Running Tests](#running-tests)

## Getting Started

### Prerequisites

Before you begin, ensure you have Python installed on your machine. This project is compatible with Python 3.6 and above.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MaruthiKo/techolution_assignment.git
   cd techolution_assignment
   ```

## Usage

To run the Library Management System, navigate to the project directory and execute the `main.py` file:

```bash
python main.py
```

### Main Menu Options

- **1. Book Management:**
  - Add, list, update, or delete books.
- **2. User Management:**
  - Add, list, update, or delete users.
- **3. Check-In/Out Management:**
  - Check out books to users or return books from users.

### Example Walkthrough

1. **Add a Book:**
   - Select `1` for Book Management.
   - Select `1` to Add Book.
   - Enter the book title, author, and ISBN.

2. **Add a User:**
   - Select `2` for User Management.
   - Select `1` to Add User.
   - Enter the user's name and user ID.

3. **Check Out a Book:**
   - Select `3` for Check-In/Out Management.
   - Select `2` to Check Out Book.
   - Enter the user ID and the book's ISBN.

## Project Structure

```
techolution_assignment/
│
├── book.py              # Handles book-related operations
├── user.py              # Handles user-related operations
├── check.py             # Handles check-in/check-out operations
├── storage.py           # Manages JSON-based persistent storage
├── main.py              # Entry point for the Library Management System
├── test_main.py         # Unit tests for the system
├── models.py            # Book, User class definition
└── README.md            # Project documentation
```

## Logging and Debugging

### Real-Time Feedback with Print Statements

This application uses `print()` statements to provide real-time feedback to the user via the command-line interface.


## Running Tests

Unit tests are provided to ensure the system functions as expected. These tests cover the core functionality, including adding, updating, and removing books and users, as well as checking books in and out.

### Running Tests with `unittest`

To run the tests, navigate to the project directory and execute:

```bash
python -m unittest test_main.py
```

### Example Unit Test

Here is an example of how the unit tests are structured:

```python
import unittest
from book import BookManager
from user import UserManager
from check import CheckManager
from models import Book, User

class TestLibraryManagementSystem(unittest.TestCase):

    @patch('storage.Storage.save_books')
    @patch('storage.Storage.load_books', return_value=[])
    def test_add_book(self, mock_load_books, mock_save_books):
        book_manager = BookManager()
        new_book = Book(title="1984", author="George Orwell", isbn="978-0451524935")
        book_manager.add_book(new_book)
        self.assertIn(new_book, book_manager.books)
        mock_save_books.assert_called_once()
    
if __name__ == '__main__':
    unittest.main()
```

### Test Coverage

- **Book Management Tests:** Adding, listing, updating, and removing books.
- **User Management Tests:** Adding, listing, updating, and removing users.
- **Check-In/Out Management Tests:** Checking books in and out.
