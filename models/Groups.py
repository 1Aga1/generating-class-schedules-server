from peewee import AutoField, TextField, ForeignKeyField
from database import BaseModel
from models import Levels


class Groups(BaseModel):
    id = AutoField(primary_key=True)
    level = ForeignKeyField(Levels, backref='groups', on_delete='CASCADE', null=False)
    name = TextField()

    def get_dto(self):
        return {
            'id': self.id,
            'level': self.level.id,
            'name': self.name,
        }

    class Meta:
        db_table = 'groups'
