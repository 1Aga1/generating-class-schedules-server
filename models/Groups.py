from peewee import AutoField, TextField, IntegerField
from database import BaseModel


class Groups(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    course = IntegerField()

    def get_dto(self):
        subjects = self.subjects.select()

        return {
            'id': self.id,
            'name': self.name,
            'course': self.course,
            'subjects': [subject.get_dto() for subject in subjects],
        }

    class Meta:
        db_table = 'groups'
