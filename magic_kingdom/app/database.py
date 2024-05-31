from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    """
    Class to configure and manage the database connection.
    """
    def __init__(self, db_url):
        """
        Initialize the Database class with the database URL.

        """
        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
    
    def get_session(self):
        """
        Get a new database session.
        """
        return self.SessionLocal()


# Database configuration
DATABASE_URL = "postgresql://jaguaru:Jaguar12345@localhost/magic_kingdom_db"

db = Database(DATABASE_URL)
