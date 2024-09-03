from storage import Storage

class UserManager:
    """
    Manage users in the library.

    Attributes:
        users (list): A list of users in the library.

    Methods:
        add_user: Add a new user to the library.
        find_user_by_id: Find a user by their ID.
        remove_user: Remove a user from the library.
        update_user: Update the details of an existing user.
        list_users: List all users in the library.

    Examples:
        user_manager = UserManager()
        new_user = User("Alice", "12345")
        user_manager.add_user(new_user)
        user_manager.list_users()
        user_manager.remove_user("12345")
    """

    def __init__(self):
        # Load users from storage during initialization
        self.users = Storage.load_users()

    def add_user(self, user):
        """
        Adds a new user to the library.

        Parameters:
            user: The user to be added.

        Returns:
            bool: True if the user is added successfully, False otherwise.
        """

        if self.find_user_by_id(user.user_id):
            print(f"User with ID {user.user_id} already exists.")
            return False
        self.users.append(user)
        Storage.save_users(self.users)
        print(f"User '{user.name}' added successfully.")
        return True

    def find_user_by_id(self, user_id):
        """
        Find a user by their ID.
        
        Parameters:
            user_id (str): The ID of the user to find.
        
        Returns:
            Object: The user is returned if found, None otherwise.
        """

        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def remove_user(self, user_id):
        """
        Remove a user from the existing users.
        
        Parameters:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if the user is removed successfully, False otherwise.
        """

        user = self.find_user_by_id(user_id)
        if user:
            self.users.remove(user)
            Storage.save_users(self.users)
            print(f"User '{user.name}' removed successfully.")
            return True
        print(f"User with ID {user_id} not found.")
        return False


    def update_user(self, user_id, name=None, new_user_id=None):
        """
        Update the details of an existing user.
        
        Parameters:
            user_id (str): The current ID of the user to update.
            name (str): New name of the user (optional).
            new_user_id (str): New ID of the user (optional).
        
        Returns:
            bool: True if the update is successful, False otherwise.
        """

        user = self.find_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            if new_user_id:
                user.user_id = new_user_id

            # Save the updated list of users
            Storage.save_users(self.users)
            print(f"User '{user.name}' updated successfully.")
            return True
        else:
            print(f"User with ID {user_id} not found.")
            return False
    

    def list_users(self):
        """
        List all users in the library.
        """
        
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users found. Add users to the library.")