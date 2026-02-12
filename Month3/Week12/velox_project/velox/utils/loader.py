"""
Velox Framework - Utility Functions
"""
import sys
import importlib
from pathlib import Path
from velox.db.models import Model


def load_app_models(app_name):
    """Load all models from an app"""
    try:
        # Import the app's models module
        models_module = importlib.import_module(f'apps.{app_name}.models')
        
        # Find all Model subclasses
        models = []
        for attr_name in dir(models_module):
            attr = getattr(models_module, attr_name)
            if isinstance(attr, type) and issubclass(attr, Model) and attr != Model:
                models.append(attr)
        
        return models
    except ImportError as e:
        print(f"Error importing models from '{app_name}': {e}")
        return []
