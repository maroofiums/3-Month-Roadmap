"""
Velox Framework - Database Models
"""
from velox.db.engine import db


class Field:
    def __init__(self, field_type, primary_key=False, unique=False, auto_increment=False):
        self.field_type = field_type
        self.primary_key = primary_key
        self.unique = unique
        self.auto_increment = auto_increment
    
    def get_sql_definition(self, field_name):
        """Get SQL definition for this field"""
        parts = [self.field_type]
        
        if self.primary_key:
            parts.append('PRIMARY KEY')
        if self.auto_increment:
            parts.append('AUTOINCREMENT')
        if self.unique and not self.primary_key:
            parts.append('UNIQUE')
        
        return ' '.join(parts)


class IntegerField(Field):
    def __init__(self, primary_key=False, auto_increment=False):
        super().__init__('INTEGER', primary_key=primary_key, auto_increment=auto_increment)


class TextField(Field):
    def __init__(self, unique=False):
        super().__init__('TEXT', unique=unique)


class ModelMeta(type):
    """Metaclass for models to collect field definitions"""
    def __new__(mcs, name, bases, attrs):
        # Collect fields
        fields = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value
                # Remove field from class attrs to avoid conflicts
                attrs.pop(key)
        
        attrs['_fields'] = fields
        attrs['_table_name'] = attrs.get('_table_name', name.lower())
        
        return super().__new__(mcs, name, bases, attrs)


class Model(metaclass=ModelMeta):
    """Base model class for database models"""
    _fields = {}
    _table_name = ''
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @classmethod
    def create_table(cls):
        """Create the table for this model"""
        field_definitions = {}
        for field_name, field in cls._fields.items():
            field_definitions[field_name] = field.get_sql_definition(field_name)
        
        db.create_table(cls._table_name, field_definitions)
    
    @classmethod
    def all(cls):
        """Get all records"""
        query = f"SELECT * FROM {cls._table_name}"
        rows = db.fetchall(query)
        return [cls(**row) for row in rows]
    
    @classmethod
    def get(cls, **kwargs):
        """Get a single record by field values"""
        conditions = [f"{k} = ?" for k in kwargs.keys()]
        condition = ' AND '.join(conditions)
        query = f"SELECT * FROM {cls._table_name} WHERE {condition}"
        row = db.fetchone(query, tuple(kwargs.values()))
        return cls(**row) if row else None
    
    @classmethod
    def filter(cls, **kwargs):
        """Filter records by field values"""
        conditions = [f"{k} = ?" for k in kwargs.keys()]
        condition = ' AND '.join(conditions)
        query = f"SELECT * FROM {cls._table_name} WHERE {condition}"
        rows = db.fetchall(query, tuple(kwargs.values()))
        return [cls(**row) for row in rows]
    
    def save(self):
        """Save the model instance"""
        data = {}
        for field_name in self._fields.keys():
            if hasattr(self, field_name):
                value = getattr(self, field_name)
                # Skip auto-increment primary keys on insert
                if self._fields[field_name].auto_increment and value is None:
                    continue
                data[field_name] = value
        
        # Check if this is an update or insert
        primary_key = self._get_primary_key_field()
        if primary_key and hasattr(self, primary_key) and getattr(self, primary_key) is not None:
            # Update
            pk_value = getattr(self, primary_key)
            update_data = {k: v for k, v in data.items() if k != primary_key}
            db.update(self._table_name, update_data, f"{primary_key} = ?", (pk_value,))
        else:
            # Insert
            pk_value = db.insert(self._table_name, data)
            if primary_key:
                setattr(self, primary_key, pk_value)
    
    def delete(self):
        """Delete the model instance"""
        primary_key = self._get_primary_key_field()
        if primary_key and hasattr(self, primary_key):
            pk_value = getattr(self, primary_key)
            db.delete(self._table_name, f"{primary_key} = ?", (pk_value,))
    
    @classmethod
    def _get_primary_key_field(cls):
        """Get the primary key field name"""
        for field_name, field in cls._fields.items():
            if field.primary_key:
                return field_name
        return None
    
    def to_dict(self):
        """Convert model instance to dictionary"""
        result = {}
        for field_name in self._fields.keys():
            if hasattr(self, field_name):
                result[field_name] = getattr(self, field_name)
        return result
