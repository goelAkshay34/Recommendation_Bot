from utils.database_utils import DatabaseUtils

# Initialize database
db_utils = DatabaseUtils()

# Insert sample users
db_utils.conn.execute("""
    INSERT OR IGNORE INTO users (username, password, interests)
    VALUES ('alice', 'password123', 'mathematics science'),
           ('bob', 'password456', 'history literature')
""")

# Insert sample learning content
db_utils.conn.execute("""
    INSERT OR IGNORE INTO content (id, description)
    VALUES ('content1', 'Introduction to Calculus'),
           ('content2', 'The History of Ancient Rome'),
           ('content3', 'Understanding Shakespeare'),
           ('content4', 'Biology Basics')
""")

db_utils.conn.commit()
print("Sample data added to the database.")
