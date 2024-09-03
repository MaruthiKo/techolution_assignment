import json
import os
from models import Book, User

class Storage:
    """
    Manage saving and loading data to and from JSON files.

    Attributes:
        BOOKS_FILE (str): The filename for the books JSON file.
        USERS_FILE (str): The filename for the users JSON file.
    
    Methods:
        save_data: Save data to a JSON file.
        load_data: Load data from a JSON file.
        save_books: Save a list of Book objects to a JSON file.
        load_books: Load a list of Book objects from a JSON file.
        save_users: Save a list of User objects to a JSON file.
        load_users: Load a list of User objects from a JSON file.
    
    Examples:
        Storage.save_books(books)
        books = Storage.load_books()
    """

    BOOKS_FILE = 'books.json'
    USERS_FILE = 'users.json'

    @staticmethod
    def save_data(data, filename):
        """
        Save data to a JSON file.

        Parameters:
            data: The data to be saved.
            filename: The name of the file to save the data to.
          
        Examples:
            Storage.save_data(books, 'books.json')
            Storage.save_data(users, 'users.json')
        """

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully saved data to {filename}.")
        except Exception as e:
            print(f"Error saving data to {filename}: {e}")


    @staticmethod
    def load_data(filename):
        """
        Load data from a JSON file.

        Parameters:
            filename: The name of the file to load the data from.
        
        Returns:
            list: The data loaded from the file.
        
        Examples:
            books = Storage.load_data('books.json')
            users = Storage.load_data('users.json')
        """

        if not os.path.exists(filename):
            print(f"{filename} does not exist. Returning an empty list.")
            return []
        
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Returning an empty list.")
            return []
        except Exception as e:
            print(f"Error loading data from {filename}: {e}")
            return []

    @staticmethod
    def save_books(books):
        """
        Save a list of Book objects to a JSON file.
        """

        book_dicts = [book.to_dict() for book in books]
        Storage.save_data(book_dicts, Storage.BOOKS_FILE)

    @staticmethod
    def load_books():
        """
        Load a list of Book objects from a JSON file.
        """

        book_dicts = Storage.load_data(Storage.BOOKS_FILE)
        return [Book.from_dict(book_dict) for book_dict in book_dicts]

    @staticmethod
    def save_users(users):
        """
        Save a list of User objects to a JSON file.
        """

        user_dicts = [user.to_dict() for user in users]
        Storage.save_data(user_dicts, Storage.USERS_FILE)

    @staticmethod
    def load_users():
        """
        Load a list of User objects from a JSON file.
        """
        
        user_dicts = Storage.load_data(Storage.USERS_FILE)
        return [User.from_dict(user_dict) for user_dict in user_dicts]
