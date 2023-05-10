from peewee import AutoField, ForeignKeyField, IntegerField
from database import BaseModel
from models import Groups, Subjects, Schedules


class ScheduleParams(BaseModel):
    id = AutoField(primary_key=True)
    schedule = ForeignKeyField(Schedules, backref='schedule_params', on_delete='CASCADE', null=False)
    group = ForeignKeyField(Groups, on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)
    number = IntegerField(null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'schedule': self.schedule.id,
            'group': self.group.id,
            'subject': self.subject.id,
            'number': self.number
        }

    class Meta:
        db_table = 'schedule_params'
