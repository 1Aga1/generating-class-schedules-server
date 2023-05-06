from peewee import AutoField, ForeignKeyField
from database import BaseModel
from models import Groups, Subjects


class GroupSubjects(BaseModel):
    id = AutoField(primary_key=True)
    group = ForeignKeyField(Groups, backref='subjects', on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'group': self.group,
            'subject': self.subject,
        }

    class Meta:
        db_table = 'group_subjects'
