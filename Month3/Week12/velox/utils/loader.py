import os
import sys
import importlib

def load_models():
    models = []

    project_root = os.getcwd()
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    if not os.path.exists("apps"):
        return models

    for app in os.listdir("apps"):
        try:
            module = importlib.import_module(f"apps.{app}.models")
        except ModuleNotFoundError:
            continue

        for attr in dir(module):
            obj = getattr(module, attr)
            if hasattr(obj, "_fields"):
                models.append(obj)

    return models
