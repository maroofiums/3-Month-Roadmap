# Velox Framework - Demo Project

A lightweight Python web framework with auto-generated CRUD endpoints.

## Project Structure

```
velox_project/
├── velox/                    # Velox Framework
│   ├── core/
│   │   ├── app.py           # Main application class
│   │   ├── router.py        # URL routing
│   │   └── response.py      # Response objects
│   ├── db/
│   │   ├── engine.py        # Database engine (SQLite)
│   │   ├── models.py        # ORM models
│   │   └── migration.py     # Migration manager
│   ├── cli/
│   │   ├── main.py          # CLI entry point
│   │   ├── project.py       # Project/app creation
│   │   └── migrate.py       # Migration commands
│   └── utils/
│       └── loader.py        # App loader utilities
│
├── demo/                     # Demo project
│   ├── apps/
│   │   └── users/
│   │       ├── __init__.py
│   │       ├── models.py    # User model
│   │       └── views.py     # CRUD endpoints
│   ├── db.sqlite3           # SQLite database (created after migration)
│   ├── main.py              # Application entry point
│   └── migrations.json      # Migration records
│
└── velox-cli.py             # CLI executable
```

## Features

- **Auto-generated CRUD endpoints** for models
- **SQLite database** support
- **Migration system** for database schema management
- **Simple routing** with URL parameters
- **JSON responses** by default
- **CLI commands** for project management

## Quick Start

### 1. Navigate to demo project

```bash
cd demo
```

### 2. Run migrations (database already set up)

The migrations.json file is already configured. To create the database tables:

```bash
cd demo
python3 -c "import sys; sys.path.insert(0, '..'); from velox.db.migration import migration_manager; migration_manager.migrate()"
```

Or simply run the server (it will auto-create tables):

### 3. Start the server

```bash
python3 main.py
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

### Users App

#### GET /hello
Returns a hello message from the users app.

```bash
curl http://127.0.0.1:8000/hello
```

Response:
```json
{"message": "Hello from Users app!"}
```

#### GET /users
List all users.

```bash
curl http://127.0.0.1:8000/users
```

Response:
```json
{
  "users": [
    {"id": 1, "name": "John Doe", "email": "john@example.com"}
  ]
}
```

#### POST /users
Create a new user.

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

Response:
```json
{
  "message": "User created successfully",
  "user": {"id": 1, "name": "John Doe", "email": "john@example.com"}
}
```

#### GET /users/<id>
Get a specific user.

```bash
curl http://127.0.0.1:8000/users/1
```

Response:
```json
{
  "user": {"id": 1, "name": "John Doe", "email": "john@example.com"}
}
```

#### PUT /users/<id>
Update a user.

```bash
curl -X PUT http://127.0.0.1:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane@example.com"}'
```

Response:
```json
{
  "message": "User updated successfully",
  "user": {"id": 1, "name": "Jane Doe", "email": "jane@example.com"}
}
```

#### DELETE /users/<id>
Delete a user.

```bash
curl -X DELETE http://127.0.0.1:8000/users/1
```

Response:
```json
{
  "message": "User deleted successfully"
}
```

## CLI Commands

### Create a new project

```bash
python3 velox-cli.py makeproject <project_name>
```

### Create a new app

```bash
cd <project_name>
python3 ../velox-cli.py makeapp <app_name>
```

### Generate migrations

```bash
cd <project_name>
python3 ../velox-cli.py makemigrations
```

### Apply migrations

```bash
cd <project_name>
python3 ../velox-cli.py migrate
```

## Creating Models

Models are defined in `apps/<app_name>/models.py`:

```python
from velox.db import Model, IntegerField, TextField

class User(Model):
    _table_name = 'users'
    
    id = IntegerField(primary_key=True, auto_increment=True)
    name = TextField()
    email = TextField(unique=True)
```

## Creating Views

Views are defined in `apps/<app_name>/views.py`:

```python
from velox.core import JsonResponse
from apps.users.models import User

def register_routes(router):
    router.add_route('GET', '/users', list_users)
    router.add_route('POST', '/users', create_user)

def list_users(request):
    users = User.all()
    return JsonResponse({
        'users': [user.to_dict() for user in users]
    })

def create_user(request):
    body = request.get('body', {})
    user = User(name=body['name'], email=body['email'])
    user.save()
    return JsonResponse({
        'message': 'User created',
        'user': user.to_dict()
    }, status_code=201)
```

## Testing the Demo

1. Start the server:
   ```bash
   cd demo
   python3 main.py
   ```

2. Test the hello endpoint:
   ```bash
   curl http://127.0.0.1:8000/hello
   ```

3. Create a user:
   ```bash
   curl -X POST http://127.0.0.1:8000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "email": "alice@example.com"}'
   ```

4. List users:
   ```bash
   curl http://127.0.0.1:8000/users
   ```

5. Get specific user:
   ```bash
   curl http://127.0.0.1:8000/users/1
   ```

6. Update user:
   ```bash
   curl -X PUT http://127.0.0.1:8000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice Updated"}'
   ```

7. Delete user:
   ```bash
   curl -X DELETE http://127.0.0.1:8000/users/1
   ```

## Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## License

MIT License
