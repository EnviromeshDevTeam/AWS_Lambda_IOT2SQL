import json
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm.session import Session
from models.data import Data
from models.device import Device
from datetime import datetime
import os

# *1. find .env file > load .env
# *2. relying on current OS (Developed in windows but Lambdas are run in Linux), get env variables of Key <String> Store as Constant
load_dotenv(find_dotenv())  # Find .env file
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWD")
DB_NAME = os.getenv("DB_NAME")
DB_ENDPOINT = os.getenv("DB_ENDPOINT")
DB_PORT = os.getenv("DB_PORT")

# From .env files grab our ENGINE_ENDPOINT or Connection string and pass it into the
DB_ENGINE = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}/{DB_NAME}")


def lambda_handler(event: str, context: str):
    """[summary]
        Activated by AWS IoT Rule triggers this Lambda
    Args:
        event (str): [Content sent from activation, This is our JSON string sent from AWS IoT]
        context (str): [Additional Context information associated with AWS internals]
    """

    # TODO Change Device in AWS IoT payload to a Device int and replace the 1 argument here
    with Session(DB_ENGINE) as db_session, db_session.begin():
        try:
            data2Insert = []
            for cat_Key, data_Value in event['data'].items():
                db_session.add(
                    Data(device_id=1, category_id=int(cat_Key), data=int(data_Value), created_at=event['timestamp'], updated_at=event['timestamp'])
                )
            device_Update = db_session.query(Device).filter(Device.id == 1).first()
            device_Update.updated_at = event['timestamp']
            db_session.commit()
            return {
                'statusCode': 200,
                'body': json.dumps('Inserted data successfully to Our DB Connection Endpoint')
            }
            
        except Exception as e:
            print(e)
            print("Something went wrong with the lambda")
            db_session.rollback()
            raise(e)
