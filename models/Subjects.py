from peewee import AutoField, TextField, ForeignKeyField
from database import BaseModel
from models import Teachers


class Subjects(BaseModel):
    id = AutoField(primary_key=True)
    name = TextField()
    teacher = ForeignKeyField(Teachers, null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'teacher': {
                'id': self.teacher.id,
                'fullname': self.teacher.fullname,
            }
        }

    class Meta:
        db_table = 'subjects'
