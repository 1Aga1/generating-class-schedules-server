from models import LevelSubjects


def add(level_id: int, subject_id: int):
    level_subject = LevelSubjects(level_id=level_id, subject_id=subject_id)
    level_subject.save()

    return level_subject.get_dto()


def remove(level_id: int, subject_id: int):
    level_subject = LevelSubjects.delete().where(LevelSubjects.level_id == level_id,
                                                 LevelSubjects.subject_id == subject_id)
    level_subject.execute()


def get_levels_subjects():
    return [levels_subject.get_dto() for levels_subject in LevelSubjects.select()]
