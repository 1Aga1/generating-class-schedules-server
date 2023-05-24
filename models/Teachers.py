from peewee import AutoField, TextField
from database import BaseModel


class Teachers(BaseModel):
    id = AutoField(primary_key=True)
    fullname = TextField()

    def get_dto(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
        }

    class Meta:
        db_table = 'teachers'
