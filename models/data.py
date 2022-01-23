from sqlalchemy import Column, Integer, TIMESTAMP, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

#Get a base model of a SqlAlchemy Object
Base=declarative_base()

class Data(Base):
    """[summary]
        Generate ORM object of each data line for sqlalchemy
    Args:
        Base ([type]): [base model of a SqlAlchemy Object]
    """
    
    #Instantiate column types ready for ORM action
    __tablename__ = os.getenv("DB_TABLE_NAME")
    id=Column(Integer, primary_key=True)
    device_id=Column(Integer)
    category_id=Column(Integer)
    data=Column(Float)
    created_at=Column(TIMESTAMP)
    updated_at=Column(TIMESTAMP)
    