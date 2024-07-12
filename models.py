# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from config import DATABASE_CONFIG

# Create an engine
engine = create_engine(f'postgresql://admin:cWR0RwyL715nufQabXHme5ou8QASIxvh@dpg-cq7vl3ggph6c73ev22bg-a.oregon-postgres.render.com/demodb_gp75', echo=True)

# Define a base class
Base = declarative_base()

# Define the User table as a class
class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        age (int): The age of the user.
        addresses (relationship): The addresses associated with the user.
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    addresses = relationship('Address', back_populates='user')

# Define the Address table as a class
class Address(Base):
    """
    Represents an address in the database.

    Attributes:
        id (int): The unique identifier of the address.
        user_id (int): The foreign key referencing the user.
        address (str): The address string.
        user (relationship): The user associated with the address.
    """
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    address = Column(String(100))
    user = relationship('User', back_populates='addresses')

# Define your table as a class
class customers(Base):
    """
    Represents a customer in the database.

    Attributes:
        id (int): The unique identifier of the customer.
        name (str): The name of the customer.
        age (int): The age of the customer.
    """
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

def create_tables():
    """
    Creates the necessary tables in the database if they don't exist.
    """
    Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
