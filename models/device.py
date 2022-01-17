from sqlalchemy import Column, Integer, DateTime, VARCHAR
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

#Get a base model of a SqlAlchemy Object
Base=declarative_base()

class Device(Base):
    """[summary]
        Generate ORM object of each data line for sqlalchemy
    Args:
        Base ([type]): [base model of a SqlAlchemy Object]
    """
    
    #Instantiate column types ready for ORM action
    __tablename__ = os.getenv('DB_TABLE_DEVICES')
    id=Column(Integer, primary_key=True)
    name=Column(VARCHAR)
    address=Column(VARCHAR)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)