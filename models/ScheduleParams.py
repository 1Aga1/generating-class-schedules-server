from peewee import AutoField, ForeignKeyField
from database import BaseModel
from models import Groups, Subjects, Schedules


class ScheduleParams(BaseModel):
    id = AutoField(primary_key=True)
    schedule = ForeignKeyField(Schedules, backref='schedule_params', on_delete='CASCADE', null=False)
    group = ForeignKeyField(Groups, on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'schedule': self.schedule,
            'group': self.group,
            'subject': self.subject,
        }

    class Meta:
        db_table = 'schedule_params'
