from .subjects import subjects
from .groups import groups
from .group_subjects import group_subjects
from .schedules import schedules
from .schedule_params import schedule_params
from .user import user
from .teachers import teachers

routes = [
    subjects.subjects_router,
    groups.groups_router,
    group_subjects.group_subjects_router,
    schedules.schedules_router,
    schedule_params.schedule_params_router,
    user.user_router,
    teachers.teachers_router
]
