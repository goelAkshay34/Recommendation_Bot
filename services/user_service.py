from utils.database_utils import DatabaseUtils

class UserService:
    def __init__(self):
        self.db_utils = DatabaseUtils()

    def authenticate(self, username, password):
        """
        Authenticates a user.
        Args:
            username (str): Username.
            password (str): Password.
        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        user = self.get_user(username)
        return user and user["password"] == password

    def get_user(self, username):
        """
        Retrieves a user from the database.
        Args:
            username (str): Username.
        Returns:
            dict: User details.
        """
        return self.db_utils.get_user(username)

    def add_user(self, username, password, interests):
        """
        Adds a new user to the database.
        Args:
            username (str): Username.
            password (str): Password.
            interests (str): User's interests.
        """
        self.db_utils.add_user(username, password, interests)
