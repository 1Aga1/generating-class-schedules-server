from .levels import levels
from .subjects import subjects
from .groups import groups
from .group_subjects import group_subjects
from .schedules import schedules
from .schedule_params import schedule_params

routes = [
    levels.level_router,
    subjects.subjects_router,
    groups.groups_router,
    group_subjects.group_subjects_router,
    schedules.schedules_router,
    schedule_params.schedule_params_router,
]
