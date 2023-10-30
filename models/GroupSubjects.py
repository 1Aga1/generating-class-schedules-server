from peewee import AutoField, ForeignKeyField
from database import BaseModel
from models import Subjects, Groups


class GroupSubjects(BaseModel):
    id = AutoField(primary_key=True)
    group = ForeignKeyField(Groups, backref='subjects', on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'group_id': self.group.id,
            'subject': {
                'id': self.subject.id,
                'name': self.subject.name,
            },
        }

    class Meta:
        db_table = 'group_subjects'
