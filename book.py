from storage import Storage

class BookManager:
    """
    Manage books in the library.

    Attributes:
        books (list): A list of books in the library.

    Methods:
        add_book: Add a new book to the library.
        find_book_by_isbn: Find a book by its ISBN.
        remove_book: Remove a book from the library.
        update_book: Update the details of an existing book.
        list_books: List all books in the
    
    Examples:
        book_manager = BookManager()
        new_book = Book("The Alchemist", "Paulo Coelho", "978-0062315007")
        book_manager.add_book(new_book)
        book_manager.list_books()
        book_manager.remove_book("978-0061122415")
    """
    def __init__(self):
        # Load books from storage during initialization
        self.books = Storage.load_books()


    def add_book(self, book):
        """
        Add a new book to the library.

        Parameters
            book: The book to be added.
        """

        self.books.append(book)
        Storage.save_books(self.books)
        print(f"Book '{book.title}' added successfully.")


    def find_book_by_isbn(self, isbn):
        """
        Find a book by its ISBN.

        Parameters:
            isbn (str): The ISBN of the book to find.

        Returns:
            Object: The book is returned if found, None otherwise.
        """

        normalized_isbn = isbn.strip()
        for b in self.books:
            if b.isbn == normalized_isbn:
                print("Book Found")
                return b
        return None

    def remove_book(self, isbn):
        """
        Remove a book from the library.

        Parameters:
            isbn (str): The ISBN of the book to remove.

        Returns: 
            bool: True if the book is removed successfully, False otherwise.
        """
        
        book = self.find_book_by_isbn(isbn)
        print(book)
        if book:
            print("Inside remove book")
            self.books.remove(book)
            Storage.save_books(self.books)
            print(f"Book '{book.title}' removed successfully.")
            return True
        print(f"Book with ISBN {isbn} not found.")
        return False
    

    def update_book(self, isbn, title=None, author=None, new_isbn=None):
        """
        Update the details of an existing book.
        
        Parameters:
            isbn (str): The ISBN of the book to update.
            title (str): New title of the book (optional).
            author (str): New author of the book (optional).
            new_isbn (str): New ISBN of the book (optional).
        
        Returns:
            True if the update is successful, False otherwise.
        """
        book = self.find_book_by_isbn(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if new_isbn:
                book.isbn = new_isbn

            # Save the updated list of books
            Storage.save_books(self.books)
            print(f"Book '{book.title}' updated successfully.")
            return True
        else:
            print(f"Book with ISBN {isbn} not found.")
            return False


    def list_books(self):
        """
        Print the list of books in the library.
        """
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available. Please add books to the library.")