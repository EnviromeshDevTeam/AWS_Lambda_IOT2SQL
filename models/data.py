from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.orm import declarative_base
from models.dtype import DType
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
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
    
    def __init__(self, _device_id:str, _data_Key:str, _data:str, _created_At:str) -> None:
        self.device_id:int = _device_id
        self.category_id:int = DType[_data_Key] #TODO: Breakpoint and test if this works?
        self.data:float = self.cast2Float(_data)
        self.created_at:datetime = _created_At 
        self.updated_at:datetime =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    
    def cast2Float(self, _item2Cast:str):
        """[summary]
            Attempt to cast str to float
        Args:
            _item2Cast (str): string from JSON

        Returns:
            [float]: cast item to float datatype of database
        """        
        try:
            return int(_item2Cast)
        except Exception as E:
            print(E)
            print("Failed Cast to FLoat")
    