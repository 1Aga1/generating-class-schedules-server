from peewee import AutoField, TextField
from database import BaseModel


class Groups(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()

    def get_dto(self):
        subjects = self.subjects.select()

        return {
            'id': self.id,
            'name': self.name,
            'subjects': [subject.get_dto() for subject in subjects],
        }

    class Meta:
        db_table = 'groups'
