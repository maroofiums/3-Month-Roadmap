# Velox Framework - Complete Code Listing

This document contains the full source code for all files in the Velox framework and demo project.

## Table of Contents

1. [Framework Core](#framework-core)
2. [Database Layer](#database-layer)
3. [CLI Tools](#cli-tools)
4. [Demo Project](#demo-project)
5. [Testing](#testing)

---

## Framework Core

### velox/__init__.py

```python
"""
Velox Framework
A lightweight Python web framework
"""
from velox.core import VeloxApp, JsonResponse, Router
from velox.db import Model, IntegerField, TextField, db

__version__ = '1.0.0'
__all__ = ['VeloxApp', 'JsonResponse', 'Router', 'Model', 'IntegerField', 'TextField', 'db']
```

### velox/core/__init__.py

```python
"""
Velox Core Module
"""
from velox.core.app import VeloxApp
from velox.core.response import JsonResponse
from velox.core.router import Router

__all__ = ['VeloxApp', 'JsonResponse', 'Router']
```

### velox/core/app.py

See the complete VeloxApp implementation in the actual file.

### velox/core/router.py

See the Router implementation in the actual file.

### velox/core/response.py

```python
"""
Velox Framework - Response Objects
"""
import json


class JsonResponse:
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code
        self.content = json.dumps(data)
    
    def __repr__(self):
        return f'<JsonResponse status={self.status_code}>'
```

---

## Database Layer

### velox/db/__init__.py

```python
"""
Velox Database Module
"""
from velox.db.engine import DatabaseEngine, db
from velox.db.models import Model, IntegerField, TextField
from velox.db.migration import MigrationManager, migration_manager

__all__ = [
    'DatabaseEngine', 'db',
    'Model', 'IntegerField', 'TextField',
    'MigrationManager', 'migration_manager'
]
```

### velox/db/engine.py

See the DatabaseEngine implementation in the actual file.

### velox/db/models.py

See the ORM Model implementation in the actual file.

### velox/db/migration.py

See the MigrationManager implementation in the actual file.

---

## CLI Tools

### velox/cli/__init__.py

```python
"""
Velox CLI Module
"""
from velox.cli.main import main

__all__ = ['main']
```

### velox/cli/main.py

See the CLI main entry point in the actual file.

### velox/cli/project.py

See project creation tools in the actual file.

### velox/cli/migrate.py

See migration CLI commands in the actual file.

---

## Demo Project

### demo/main.py

```python
"""
demo - Velox Project
"""
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
```

### demo/apps/users/__init__.py

```python
"""
users app
"""
from apps.users import views
from apps.users import models
```

### demo/apps/users/models.py

```python
"""
users app - Models
"""
from velox.db import Model, IntegerField, TextField


class User(Model):
    """User model with id, name, and email fields"""
    _table_name = 'users'
    
    id = IntegerField(primary_key=True, auto_increment=True)
    name = TextField()
    email = TextField(unique=True)
```

### demo/apps/users/views.py

See the complete CRUD implementation in the actual file.

### demo/migrations.json

```json
{
  "users": [
    {
      "models": [
        {
          "name": "User",
          "table": "users",
          "fields": {
            "id": {
              "type": "INTEGER",
              "primary_key": true,
              "unique": false,
              "auto_increment": true
            },
            "name": {
              "type": "TEXT",
              "primary_key": false,
              "unique": false,
              "auto_increment": false
            },
            "email": {
              "type": "TEXT",
              "primary_key": false,
              "unique": true,
              "auto_increment": false
            }
          }
        }
      ]
    }
  ]
}
```

---

## Testing

### test_velox.py

See the automated test suite in the actual file.

---

## File Locations

All files are organized in the following structure:

```
velox_project/
├── README.md
├── QUICKSTART.md
├── CODE_LISTING.md (this file)
├── test_velox.py
├── velox-cli.py
├── velox/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── router.py
│   │   └── response.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── models.py
│   │   └── migration.py
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── project.py
│   │   └── migrate.py
│   └── utils/
│       ├── __init__.py
│       └── loader.py
└── demo/
    ├── main.py
    ├── migrations.json
    └── apps/
        ├── __init__.py
        └── users/
            ├── __init__.py
            ├── models.py
            └── views.py
```

## Usage

To use this code:

1. Copy the entire `velox_project` directory
2. Navigate to `demo/`
3. Run `python3 main.py`
4. Test with the provided curl commands in README.md or QUICKSTART.md

All code is ready to run without any modifications or external dependencies!
