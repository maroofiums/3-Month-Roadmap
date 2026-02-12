"""
Velox Demo Server - Run this file to start the server
"""
import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Change to demo directory for database file
demo_dir = os.path.join(project_root, 'demo')
os.chdir(demo_dir)

from velox.core import VeloxApp
from velox.db import db

# Create Velox app
app = VeloxApp('demo')

# Import and register apps
from apps import users
app.add_app(users)

if __name__ == '__main__':
    print("Starting Velox Demo Server...")
    print(f"Working directory: {os.getcwd()}")
    print(f"Python path includes: {project_root}")
    print()
    
    # Connect to database
    db.connect()
    
    # Run migrations if needed
    from velox.db.migration import migration_manager
    try:
        migration_manager.migrate()
    except:
        pass  # Tables may already exist
    
    # Run the server
    app.run(host='127.0.0.1', port=8000)
