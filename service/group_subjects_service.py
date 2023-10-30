from models import GroupSubjects


def add(group_id: int, subject_id: int):
    group_subject = GroupSubjects(group=group_id, subject_id=subject_id)
    group_subject.save()

    return group_subject.get_dto()


def remove(level_id: int, subject_id: int):
    group_subject = GroupSubjects.delete().where(GroupSubjects.group_id == level_id,
                                                 GroupSubjects.subject_id == subject_id)
    group_subject.execute()


def get_groups_subjects():
    return [groups_subject.get_dto() for groups_subject in GroupSubjects.select()]
