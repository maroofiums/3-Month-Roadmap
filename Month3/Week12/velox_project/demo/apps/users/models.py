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
