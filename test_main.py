import unittest
from unittest.mock import patch
from book import BookManager
from user import UserManager
from check import CheckManager
from models import Book
from models import User

class TestLibraryManagementSystem(unittest.TestCase):
    """
    Unit tests for the Library Management System.

    The tests are written to ensure that the system behaves as expected.

    Methods:
        test_add_book: Test adding a new book to the library.
        test_remove_book: Test removing a book from the library.
        test_add_user: Test adding a new user to the library.
        test_remove_user: Test removing a user from the library.
        test_checkout_book: Test checking out a book for a user.
        test_return_book: Test returning a book that was checked out.
    """

    @patch('storage.Storage.save_books')
    @patch('storage.Storage.load_books', return_value=[])
    def test_add_book(self, mock_load_books, mock_save_books):
        book_manager = BookManager()
        new_book = Book(title="1984", author="George Orwell", isbn="978-0451524935")
        book_manager.add_book(new_book)
        self.assertIn(new_book, book_manager.books)
        mock_save_books.assert_called_once()

    @patch('storage.Storage.save_books')
    @patch('storage.Storage.load_books', return_value=[Book(title="1984", author="George Orwell", isbn="978-0451524935")])
    def test_remove_book(self, mock_load_books, mock_save_books):
        book_manager = BookManager()
        book_manager.remove_book(isbn="978-0451524935")
        self.assertNotIn(Book(title="1984", author="George Orwell", isbn="978-0451524935"), book_manager.books)
        mock_save_books.assert_called_once()

    @patch('storage.Storage.save_users')
    @patch('storage.Storage.load_users', return_value=[])
    def test_add_user(self, mock_load_users, mock_save_users):
        user_manager = UserManager()
        new_user = User(name="Alice Smith", user_id="U1001")
        user_manager.add_user(new_user)
        self.assertIn(new_user, user_manager.users)
        mock_save_users.assert_called_once()

    @patch('storage.Storage.save_users')
    @patch('storage.Storage.load_users', return_value=[User(name="Alice Smith", user_id="U1001")])
    def test_remove_user(self, mock_load_users, mock_save_users):
        user_manager = UserManager()
        user_manager.remove_user(user_id="U1001")
        self.assertNotIn(User(name="Alice Smith", user_id="U1001"), user_manager.users)
        mock_save_users.assert_called_once()

    @patch('storage.Storage.save_books')
    @patch('storage.Storage.load_books', return_value=[Book(title="1984", author="George Orwell", isbn="978-0451524935")])
    @patch('storage.Storage.save_users')
    @patch('storage.Storage.load_users', return_value=[User(name="Alice Smith", user_id="U1001")])
    def test_checkout_book(self, mock_load_books, mock_save_books, mock_load_users, mock_save_users):
        book_manager = BookManager()
        user_manager = UserManager()
        check_manager = CheckManager(book_manager, user_manager)
        check_manager.check_out_book(user_id="U1001", isbn="978-0451524935")
        self.assertTrue(book_manager.find_book_by_isbn("978-0451524935")._is_checked_out)

    @patch('storage.Storage.save_books')
    @patch('storage.Storage.load_books', return_value=[Book(title="1984", author="George Orwell", isbn="978-0451524935", is_checked_out=True)])
    @patch('storage.Storage.save_users')
    @patch('storage.Storage.load_users', return_value=[User(name="Alice Smith", user_id="U1001", borrowed_books=["978-0451524935"])])
    def test_return_book(self, mock_load_books, mock_save_books, mock_load_users, mock_save_users):
        book_manager = BookManager()
        user_manager = UserManager()
        check_manager = CheckManager(book_manager, user_manager)
        check_manager.return_book(user_id="U1001", isbn="978-0451524935")
        self.assertFalse(book_manager.find_book_by_isbn("978-0451524935")._is_checked_out)


if __name__ == '__main__':
    unittest.main()
