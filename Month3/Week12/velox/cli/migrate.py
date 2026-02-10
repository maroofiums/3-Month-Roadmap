from velox.db.migration import makemigrations, migrate
from velox.utils.loader import load_models

def makemigrations_cmd():
    models = load_models()
    makemigrations(models)

def migrate_cmd():
    migrate()
