from models import GroupSubjects


def add(group_id: int, subject_id: int):
    group_subject = GroupSubjects(group_id=group_id, subject_id=subject_id)
    group_subject.save()

    return group_subject.get_dto()


def remove(group_id: int, subject_id: int):
    group_subject = GroupSubjects.delete().where(GroupSubjects.group_id == group_id,
                                                 GroupSubjects.subject_id == subject_id)
    group_subject.execute()


def get():
    return [group_subject.get_dto() for group_subject in GroupSubjects.select()]
