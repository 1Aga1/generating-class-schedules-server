from .levels import levels
from .subjects import subjects


routes = [
    levels.level_router,
    subjects.subjects_router
]
