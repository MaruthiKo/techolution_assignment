class CheckManager:
    """
    Manages the checking out and returning of books for users.

    Attributes:
        book_manager (BookManager): An instance of BookManager.
        user_manager (UserManager): An instance of UserManager.
    
    Methods:
        check_out_book: Check out a book for a user.
        return_book: Return a book that was checked out.
    
    Examples:
        book_manager = BookManager()
        user_manager = UserManager()
        check_manager = CheckManager(book_manager, user_manager)
        check_manager.check_out_book("12345", "978-0061122415")
        check_manager.return_book("12345", "978-0061122415")
    """

    def __init__(self, book_manager, user_manager):
        """
        Initialize the CheckManager with instances of BookManager and UserManager.
        """

        self.book_manager = book_manager
        self.user_manager = user_manager


    def check_out_book(self, user_id, isbn):
        """
        Check out a book for a user.
        
        Parameters:
            user_id: The ID of the user checking out the book.
            isbn: The ISBN of the book to be checked out.

        Returns:
            bool: True if the checkout is successful, False otherwise.
        """

        user = self.user_manager.find_user_by_id(user_id)
        if not user:
            print(f"User with ID {user_id} not found.")
            return False
        
        book = self.book_manager.find_book_by_isbn(isbn)
        print(book)
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return False
        
        if book.check_out():  # Use the Book's check_out method
            if user.borrow_book(book):  # Call borrow_book on the user object
                self.book_manager.remove_book(isbn)
                self.book_manager.add_book(book)  # Update the book's status in storage
                print(f"Book '{book.title}' (ISBN: {isbn}) checked out by {user.name} (ID: {user_id}).")
                return True
            else:
                book.check_in()  # Revert the checkout if the user cannot borrow
        print(f"Failed to check out book '{book.title}' (ISBN: {isbn}) for {user.name} (ID: {user_id}).")
        return False


    def return_book(self, user_id, isbn):
        """
        Return a book that was checked out.
        
        Parameters:
            user_id (str): The ID of the user returning the book.
            isbn (str): The ISBN of the book to be returned.

        Returns:
            bool: True if the return is successful, False otherwise.
        """
        
        user = self.user_manager.find_user_by_id(user_id)
        if not user:
            print(f"User with ID {user_id} not found.")
            return False
        
        book = self.book_manager.find_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return False
        
        if book.check_in():  # Use the Book's check_in method
            if user.return_book(book):  # Call return_book on the user object
                self.book_manager.remove_book(isbn)
                self.book_manager.add_book(book)  # Update the book's status in storage
                print(f"Book '{book.title}' (ISBN: {isbn}) returned by {user.name} (ID: {user_id}).")
                return True
            else:
                book.check_out()  # Revert the check-in if the user cannot return
        print(f"Failed to return book '{book.title}' (ISBN: {isbn}) for {user.name} (ID: {user_id}).")
        return False