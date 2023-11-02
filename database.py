import os
from peewee import MySQLDatabase, Model
from dotenv import load_dotenv

load_dotenv()

db = MySQLDatabase(
    os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    host=os.environ.get('DB_HOST'),
    password=os.environ.get('DB_PASSWORD'),
    port=int(os.environ.get('DB_PORT')),
    autoconnect=False
)


class BaseModel(Model):
    class Meta:
        database = db
