"""
demo - Velox Project
"""
import sys
import os
from pathlib import Path

# Add parent directory to Python path so velox module can be imported
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from velox.core import VeloxApp
from velox.db import db

# Create Velox app
app = VeloxApp('demo')

# Import and register apps
from apps import users
app.add_app(users)

if __name__ == '__main__':
    # Connect to database
    db.connect()
    
    # Run the server
    app.run(host='127.0.0.1', port=8000)
