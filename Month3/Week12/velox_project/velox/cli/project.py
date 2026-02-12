"""
Velox Framework - Project and App Creation
"""
import os
from pathlib import Path


def create_project(project_name):
    """Create a new Velox project"""
    project_dir = Path(project_name)
    
    if project_dir.exists():
        print(f"Error: Directory '{project_name}' already exists")
        return
    
    # Create project structure
    project_dir.mkdir()
    (project_dir / 'apps').mkdir()
    
    # Create main.py
    main_content = f'''"""
{project_name} - Velox Project
"""
from velox.core import VeloxApp
from velox.db import db

# Create Velox app
app = VeloxApp('{project_name}')

# Import and register apps here
# Example:
# from apps import users
# app.add_app(users)

if __name__ == '__main__':
    # Connect to database
    db.connect()
    
    # Run the server
    app.run(host='127.0.0.1', port=8000)
'''
    
    with open(project_dir / 'main.py', 'w') as f:
        f.write(main_content)
    
    # Create migrations.json
    with open(project_dir / 'migrations.json', 'w') as f:
        f.write('{}')
    
    print(f"Created project '{project_name}'")
    print(f"  {project_name}/")
    print(f"    apps/")
    print(f"    main.py")
    print(f"    migrations.json")


def create_app(app_name):
    """Create a new app in the current project"""
    apps_dir = Path('apps')
    
    if not apps_dir.exists():
        print("Error: Not in a Velox project directory (apps/ not found)")
        return
    
    app_dir = apps_dir / app_name
    
    if app_dir.exists():
        print(f"Error: App '{app_name}' already exists")
        return
    
    # Create app directory
    app_dir.mkdir()
    
    # Create __init__.py
    init_content = f'''"""
{app_name} app
"""
from apps.{app_name} import views
from apps.{app_name} import models
'''
    
    with open(app_dir / '__init__.py', 'w') as f:
        f.write(init_content)
    
    # Create models.py
    models_content = f'''"""
{app_name} app - Models
"""
from velox.db import Model, IntegerField, TextField


# Define your models here
# Example:
# class MyModel(Model):
#     id = IntegerField(primary_key=True, auto_increment=True)
#     name = TextField()
'''
    
    with open(app_dir / 'models.py', 'w') as f:
        f.write(models_content)
    
    # Create views.py
    views_content = f'''"""
{app_name} app - Views
"""
from velox.core import JsonResponse


def register_routes(router):
    """Register app routes"""
    # Example route
    router.add_route('GET', '/{app_name}/hello', hello)


def hello(request):
    """Example view"""
    return {{"message": "Hello from {app_name} app!"}}
'''
    
    with open(app_dir / 'views.py', 'w') as f:
        f.write(views_content)
    
    print(f"Created app '{app_name}'")
    print(f"  apps/{app_name}/")
    print(f"    __init__.py")
    print(f"    models.py")
    print(f"    views.py")
    print(f"\nDon't forget to:")
    print(f"  1. Add your app to main.py:")
    print(f"     from apps import {app_name}")
    print(f"     app.add_app({app_name})")
