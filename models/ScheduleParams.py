from peewee import AutoField, ForeignKeyField, IntegerField
from database import BaseModel
from models import Groups, Subjects, Schedules


class ScheduleParams(BaseModel):
    id = AutoField(primary_key=True)
    schedule = ForeignKeyField(Schedules, backref='schedule_params', on_delete='CASCADE', null=False)
    group = ForeignKeyField(Groups, on_delete='CASCADE', null=False)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)
    number = IntegerField(null=False)
    office = IntegerField(null=True)

    def get_dto(self):
        return {
            'id': self.id,
            'schedule_id': self.schedule.id,
            'group_id': self.group.id,
            'subject_id': self.subject.id,
            'number': self.number,
            'office': self.office,
        }

    class Meta:
        db_table = 'schedule_params'
