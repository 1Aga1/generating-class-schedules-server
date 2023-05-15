from .levels import levels
from .subjects import subjects
from .groups import groups
from .level_subjects import level_subjects
from .schedules import schedules
from .schedule_params import schedule_params
from .user import user
from .document import document

routes = [
    levels.level_router,
    subjects.subjects_router,
    groups.groups_router,
    level_subjects.level_subjects_router,
    schedules.schedules_router,
    schedule_params.schedule_params_router,
    user.user_router,
    document.document_router
]
