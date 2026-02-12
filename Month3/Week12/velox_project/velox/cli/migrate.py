"""
Velox Framework - Migration CLI Commands
"""
import sys
import importlib
from pathlib import Path
from velox.db.migration import migration_manager
from velox.utils.loader import load_app_models


def make_migrations():
    """Create migrations for all apps"""
    apps_dir = Path('apps')
    
    if not apps_dir.exists():
        print("Error: Not in a Velox project directory (apps/ not found)")
        return
    
    # Find all apps
    app_dirs = [d for d in apps_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]
    
    if not app_dirs:
        print("No apps found")
        return
    
    for app_dir in app_dirs:
        app_name = app_dir.name
        models = load_app_models(app_name)
        
        if models:
            migration_manager.make_migrations(app_name, models)
            print(f"Created migrations for '{app_name}'")
        else:
            print(f"No models found in '{app_name}'")
    
    print("\nMigrations created successfully!")


def migrate():
    """Apply all migrations"""
    if not Path('migrations.json').exists():
        print("No migrations found. Run 'velox makemigrations' first.")
        return
    
    migration_manager.migrate()
