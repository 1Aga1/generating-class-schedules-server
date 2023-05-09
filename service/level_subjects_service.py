from models import LevelSubjects


def add(level_id: int, subject_id: int):
    level_subject = LevelSubjects(level_id=level_id, subject_id=subject_id)
    level_subject.save()

    return level_subject.get_dto()


def remove(level_id: int, subject_id: int):
    level_subject = LevelSubjects.delete().where(LevelSubjects.level_id == level_id,
                                                 LevelSubjects.subject_id == subject_id)
    level_subject.execute()


def get_level_subjects(level_id: int):
    return [level_subject.get_dto() for level_subject in LevelSubjects.select().where(LevelSubjects.level == level_id)]
