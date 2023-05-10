from peewee import AutoField, DateField
from database import BaseModel


class Schedules(BaseModel):
    id = AutoField(primary_key=True)
    date = DateField()

    def get_dto(self):
        return {
            'id': self.id,
            'date': self.date,
        }

    class Meta:
        db_table = 'schedules'
