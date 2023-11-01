from peewee import AutoField, DateField, BooleanField
from database import BaseModel


class Schedules(BaseModel):
    id = AutoField(primary_key=True)
    date = DateField()
    visible = BooleanField()

    def get_dto(self):
        return {
            'id': self.id,
            'date': self.date,
            'visible': self.visible
        }

    class Meta:
        db_table = 'schedules'
