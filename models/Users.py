from peewee import AutoField, TextField
from database import BaseModel


class Users(BaseModel):
    id = AutoField(primary_key=True)
    username = TextField()
    password = TextField()
    session = TextField()

    def get_dto(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'session': self.session,
        }

    class Meta:
        db_table = 'users'
