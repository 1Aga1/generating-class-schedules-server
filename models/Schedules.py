from peewee import AutoField, DateField
from database import BaseModel


class Schedules(BaseModel):
    id = AutoField(primary_key=True)
    date = DateField()

    def get_dto(self):
        params = self.schedule_params.select()

        return {
            'id': self.id,
            'date': self.date,
            'params': [param.get_dto() for param in params]
        }

    class Meta:
        db_table = 'schedules'
