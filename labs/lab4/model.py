import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    balance = Column(Integer, nullable=False)
    public_key = Column(String(250), nullable=False)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
 
# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
 
# # Create an engine that stores data in the local directory's
# # sqlalchemy_example.db file.
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///sqlalchemy_example.db')
 
# # Create all tables in the engine. This is equivalent to "Create Table"
# # statements in raw SQL.
# Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker
# DBSession = sessionmaker(bind=engine)

# session = DBSession()