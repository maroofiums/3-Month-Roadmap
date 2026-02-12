# Velox Framework - Quick Start Guide

## Installation

No installation required! The framework uses only Python standard library.

## Running the Demo Project

### Option 1: Quick Test (Automated)

```bash
cd velox_project
python3 test_velox.py
```

This will:
- Start the server
- Run automated API tests
- Display all test results
- Automatically shut down

### Option 2: Manual Start

```bash
cd velox_project/demo
python3 main.py
```

The server will start at `http://127.0.0.1:8000`

## Testing the API

Once the server is running, try these commands in a new terminal:

### 1. Test Hello Endpoint
```bash
curl http://127.0.0.1:8000/hello
```

### 2. Create a User
```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### 3. List All Users
```bash
curl http://127.0.0.1:8000/users
```

### 4. Get Specific User
```bash
curl http://127.0.0.1:8000/users/1
```

### 5. Update User
```bash
curl -X PUT http://127.0.0.1:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe"}'
```

### 6. Delete User
```bash
curl -X DELETE http://127.0.0.1:8000/users/1
```

## File Structure

```
velox_project/
├── README.md                 # Detailed documentation
├── QUICKSTART.md            # This file
├── test_velox.py            # Automated test suite
├── velox-cli.py             # CLI tool
│
├── velox/                   # Framework code
│   ├── __init__.py
│   ├── core/               # Core application
│   │   ├── __init__.py
│   │   ├── app.py         # VeloxApp class
│   │   ├── router.py      # URL routing
│   │   └── response.py    # JsonResponse class
│   ├── db/                # Database layer
│   │   ├── __init__.py
│   │   ├── engine.py      # SQLite engine
│   │   ├── models.py      # ORM models
│   │   └── migration.py   # Migrations
│   ├── cli/               # CLI commands
│   │   ├── __init__.py
│   │   ├── main.py        # CLI entry
│   │   ├── project.py     # Project creation
│   │   └── migrate.py     # Migration commands
│   └── utils/             # Utilities
│       ├── __init__.py
│       └── loader.py      # Model loader
│
└── demo/                   # Example project
    ├── main.py            # Server entry point
    ├── migrations.json    # Database migrations
    ├── db.sqlite3         # Database (created on first run)
    └── apps/
        ├── __init__.py
        └── users/         # Users app
            ├── __init__.py
            ├── models.py  # User model
            └── views.py   # CRUD endpoints
```

## Creating New Projects

### 1. Create Project
```bash
cd velox_project
python3 velox-cli.py makeproject myproject
```

### 2. Create App
```bash
cd myproject
python3 ../velox-cli.py makeapp myapp
```

### 3. Define Models
Edit `apps/myapp/models.py`:

```python
from velox.db import Model, IntegerField, TextField

class MyModel(Model):
    _table_name = 'mymodel'
    
    id = IntegerField(primary_key=True, auto_increment=True)
    title = TextField()
    description = TextField()
```

### 4. Create Views
Edit `apps/myapp/views.py`:

```python
from velox.core import JsonResponse
from apps.myapp.models import MyModel

def register_routes(router):
    router.add_route('GET', '/items', list_items)
    router.add_route('POST', '/items', create_item)

def list_items(request):
    items = MyModel.all()
    return JsonResponse({
        'items': [item.to_dict() for item in items]
    })

def create_item(request):
    body = request.get('body', {})
    item = MyModel(**body)
    item.save()
    return JsonResponse({
        'item': item.to_dict()
    }, status_code=201)
```

### 5. Register App
Edit `main.py`:

```python
from apps import myapp
app.add_app(myapp)
```

### 6. Run Migrations
```bash
python3 ../velox-cli.py makemigrations
python3 ../velox-cli.py migrate
```

### 7. Start Server
```bash
python3 main.py
```

## Requirements

- Python 3.7 or higher
- No external dependencies

## Features

✓ Auto-generated CRUD endpoints
✓ SQLite database support
✓ Simple ORM with Model class
✓ Migration system
✓ URL routing with parameters
✓ JSON responses by default
✓ CLI for project management
✓ No external dependencies

## Next Steps

- Read the full README.md for detailed documentation
- Explore the demo project code
- Create your own project and apps
- Customize the framework to your needs

Enjoy using Velox! 🚀
