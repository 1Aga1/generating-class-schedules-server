from peewee import AutoField, ForeignKeyField
from database import BaseModel
from models import Subjects, Levels


class LevelSubjects(BaseModel):
    id = AutoField(primary_key=True)
    level = ForeignKeyField(Levels, backref='subjects', on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'level': self.level.id,
            'subject': {
                'id': self.subject.id,
                'name': self.subject.name,
                'office': self.subject.office,
            },
        }

    class Meta:
        db_table = 'level_subjects'
