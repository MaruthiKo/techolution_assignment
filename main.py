from book import BookManager
from user import UserManager
from check import CheckManager
from models import Book, User, output_decorator


@output_decorator
def book_menu():
    print("\nBook Management Menu\n")

    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")


@output_decorator
def user_menu():
    print("\nUser Management Menu\n")

    print("1. Add User")
    print("2. List Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")


@output_decorator
def check_menu():
    print("\nCheck In/Out Management Menu\n")
    print("1. Check In Book")
    print("2. Check Out Book")
    print("3. Exit")


def main_menu():
    print("\nWelcome to the New World Library. Please select an option (Enter only the number)\n")
    while True:
        print("1. Book Management")
        print("2. User Management")
        print("3. Check Out Management")
        choice1 = input("Enter choice: ")
        if choice1 == '1': # Book Management
            book_menu()
        elif choice1 == '2': # User Management
            user_menu()
        elif choice1 == '3': # Check Out Management
            check_menu()
        else:
            print("\nIt seems you have entered an invalid option. Please enter an option from the list.\n")
            continue
        choice2 = input("\nPlease, select an option from the above list (Enter only the number): ")
        return (choice1, choice2)


def main():
    book_manager = BookManager()
    user_manager = UserManager()
    check_manager = CheckManager(book_manager, user_manager)
    while True:
        choice1, choice2 = main_menu() # choice1 => Management Menu choice, choice2 => Sub Menu choice
        
        if choice1 == '1': # Book Management
            if choice2 == '1': # Add Book
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ").strip()
                new_book = Book(title=title, author=author, isbn=isbn)
                book_manager.add_book(new_book)
        
            elif choice2 == '2': # List Books
                print("\nList of Books:")
                book_manager.list_books()
            
            elif choice2 == '3': # Update Book
                isbn = input("Enter ISBN of the book to update: ").strip()
                title = input("Enter new title (Press Enter to skip): ")
                author = input("Enter new author (Press Enter to skip): ")
                new_isbn = input("Enter new ISBN (Press Enter to skip): ").strip()
                print("\nUpdating the details of the book...")
                book_manager.update_book(isbn=isbn, title=title, author=author, new_isbn=new_isbn)
            
            elif choice2 == '4': # Delete Book
                isbn = input("Enter ISBN of the book to delete: ").strip()
                print("\nDeleting the book...")
                book_manager.remove_book(isbn)

            elif choice2 == '5':
                print("\nThank you for visiting the New World Library. Goodbye, Have a nice day!\n")
                break

        elif choice1 == '2': # User Management
            if choice2 == '1': # Add User
                print("\nAdding a new user...\n")
                print("\nPlease enter the following details:")
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                new_user = User(name=name, user_id=user_id)
                user_manager.add_user(new_user)
            
            elif choice2 == '2': # List Users
                print("\nList of Users:\n")
                user_manager.list_users()
            
            elif choice2 == '3': # Update User
                user_id = input("Enter user ID of the user to update: ")
                name = input("Enter new name (Press Enter to skip): ")
                new_user_id = input("Enter new user ID (Press Enter to skip): ")
                print("\nUpdating the details of the user...\n")
                user_manager.update_user(user_id=user_id, name=name, new_user_id=new_user_id)
            
            elif choice2 == '4': # Delete User
                user_id = input("Enter user ID of the user to delete: ")
                print("\nDeleting the user...\n")
                user_manager.remove_user(user_id)
            
            elif choice2 == '5':
                print("\nThank you for visiting the New World Library. Goodbye, Have a nice day!\n")
                break

        elif choice1 == '3': # Check In/Out Management
            if choice2 == '1': # Check In Book
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ").strip()
                print("\nChecking in a book...")
                check_manager.return_book(user_id=user_id, isbn=isbn)

            elif choice2 == '2': # Check Out Book
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ").strip()
                print("\nChecking out a book...")
                check_manager.check_out_book(user_id=user_id, isbn=isbn)
        
            elif choice2 == '3': # Exit
                print("\nThank you for visiting the New World Library. Goodbye, Have a nice day!\n")
                break

        else: # Invalid Option
            print("\nIt seems you have entered an invalid option. Please enter an option from the list.\n")

if __name__ == "__main__":
    main()