import sqlite3
from config.settings import DATABASE_PATH

class DatabaseUtils:
    def _initialize_db(self):
        """
        Initializes the database schema.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    interests TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS content (
                    id TEXT PRIMARY KEY,
                    description TEXT
                )
            """)
            conn.commit()

    def get_user(self, username):
        """
        Retrieves a user from the database.
        Args:
            username (str): Username.
        Returns:
            dict: User details.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            row = cursor.fetchone()
            if row:
                return {"username": row[0], "password": row[1], "interests": row[2]}
            return None

    def add_user(self, username, password, interests):
        """
        Adds a new user to the database.
        Args:
            username (str): Username.
            password (str): Password.
            interests (str): User's interests.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, password, interests)
                VALUES (?, ?, ?)
            """, (username, password, interests))
            conn.commit()

    def get_all_content(self):
        """
        Retrieves all learning content from the database.
        Returns:
            list: List of content dictionaries.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM content")
            rows = cursor.fetchall()
            return [{"id": row[0], "description": row[1]} for row in rows]
        
    def get_content_by_id(self, content_id):
        """
        Retrieves content details by ID.
        Args:
            content_id (str): Content ID.
        Returns:
            dict: Content details.
        """
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM content WHERE id=?", (content_id,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "description": row[1]}
            return None
