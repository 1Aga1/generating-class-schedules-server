from peewee import AutoField, TextField
from database import BaseModel


class Levels(BaseModel):
    id = AutoField(primary_key=True)
    text = TextField()

    def get_dto(self):
        groups = self.groups.select()
        subjects = self.subjects.select()

        return {
            'id': self.id,
            'text': self.text,
            'groups': [group.get_dto() for group in groups],
            'subjects': [subject.get_dto() for subject in subjects]
        }

    class Meta:
        db_table = 'levels'
