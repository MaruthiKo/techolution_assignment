import functools
import io
import sys

class Book:
    """
    A class to represent a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        is_checked_out (bool): The status of the book (checked out or not).
    
    Methods:
        __str__(): Return a string representation of the book.
        to_dict(): Convert the Book object to a dictionary.
        from_dict(data): Create a Book object from a dictionary.
    
    Examples:
        new_book = Book("The Alchemist", "Paulo Coelho", "978-0062315007")
        print(new_book)
        # Output: Book: The Alchemist by Paulo Coelho (ISBN: 978-0062315007) - Available
    """
    def __init__(self, title, author, isbn, is_checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn.strip()
        self._is_checked_out = is_checked_out

    def __str__(self):
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) - {status}" 
    
    def check_out(self):
        """
        Mark the book as checked out if it is not already checked out.
        
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """

        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    

    def check_in(self):
        """
        Mark the book as checked in if it is currently checked out.
        
        Returns:
            bool: True if the book was successfully checked in, False otherwise.
        """
        
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    

    def to_dict(self):
        """
        Convert the Book object to a dictionary.
        
        Returns:
            dict: A dictionary representation of the Book object.
        """

        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn.strip(),
            'is_checked_out': self._is_checked_out
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Book object from a dictionary.

        Parameters:
            data (dict): A dictionary containing the book details.
        
        Returns:
            Book: A Book object created from the dictionary
        """

        return Book(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'].strip(),
            is_checked_out=data.get('is_checked_out', False)
        )


class User:
    """
    A class to represent a user in the library.
    
    Attributes:
        name (str): The name of the user.
        user_id (str): The ID of the user.
        borrowed_books (list): A list of books borrowed by the user.
    
    Methods:
        __str__(): Return a string representation of the user.
        borrow_book(book): Add a book to the user's borrowed books list.
        return_book(book): Remove a book from the user's borrowed books list
        to_dict(): Convert the User object to a dictionary.
        from_dict(data): Create a User object from a dictionary.
    
    Examples:
        new_user = User("Alice", "12345")
        print(new_user)
        # Output: User: Alice (ID: 12345)
    """
    def __init__(self, name, user_id, borrowed_books=None):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __str__(self):
        borrowed_books_str = ', '.join(self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f"User: {self.name} (ID: {self.user_id}) - Borrowed Books: {borrowed_books_str}"

    def borrow_book(self, book):
        """
        Add the book's ISBN to the user's borrowed books list.
        
        :param book: Book object to be borrowed.
        :return: True if the book is successfully borrowed, False otherwise.
        """
        if book.isbn not in self.borrowed_books:
            self.borrowed_books.append(book.isbn)
            return True
        return False
    
    def return_book(self, book):
        """
        Remove the book's ISBN from the user's borrowed books list.
        
        Parameters:
            book (Object): Book object to be returned.

        Returns:
            bool : True if the book is successfully returned, False otherwise.
        """
        if book.isbn in self.borrowed_books:
            self.borrowed_books.remove(book.isbn)
            return True
        return False

    def to_dict(self):
        """
        Convert the User object to a dictionary.
        
        Returns:
            dict: A dictionary representation of the User object.
        """

        return {
            'name': self.name,
            'user_id': self.user_id,
            'borrowed_books': self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        """
        Create a User object from a dictionary.
        
        Parameters:
            data (dict): A dictionary containing the user details.
        
        Returns:
            User: A User object created from the dictionary
        """
        
        return User(
            name=data['name'],
            user_id=data['user_id'],
            borrowed_books=data.get('borrowed_books', [])
        )


def output_decorator(func):
    """
    A decorator that adds a border around the output of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Capture the output of the function
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        try:
            func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout

        # Get the captured output
        output = new_stdout.getvalue()

        # Print the output with the border
        print("--------------------")
        print(output, end='')
        print("--------------------")

    return wrapper