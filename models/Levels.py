from peewee import AutoField, TextField
from database import BaseModel


class Levels(BaseModel):
    id = AutoField(primary_key=True)
    text = TextField()

    def get_dto(self):
        return {
            'id': self.id,
            'text': self.text,
        }

    class Meta:
        db_table = 'levels'
