from peewee import AutoField, ForeignKeyField, IntegerField, TextField
from database import BaseModel
from models import Groups, Subjects, Schedules


class ScheduleParams(BaseModel):
    id = AutoField(primary_key=True)
    schedule = ForeignKeyField(Schedules, backref='schedule_params', on_delete='CASCADE', null=False)
    group = ForeignKeyField(Groups, on_delete='CASCADE', null=False)
    sub_group = TextField(null=True)
    subject = ForeignKeyField(Subjects, on_delete='CASCADE', null=False)
    first_half = TextField(null=True)
    number = IntegerField(null=False)
    office = IntegerField(null=False)

    def get_dto(self):
        return {
            'id': self.id,
            'schedule_id': self.schedule.id,
            'group_id': self.group.id,
            'sub_group': self.sub_group,
            'subject_id': self.subject.id,
            'first_half': self.first_half,
            'number': self.number,
            'office': self.office,
        }

    class Meta:
        db_table = 'schedule_params'
