from peewee import AutoField, TextField
from database import BaseModel


class Subjects(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    office = TextField()

    def get_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'office': self.office,
        }

    class Meta:
        db_table = 'subjects'
