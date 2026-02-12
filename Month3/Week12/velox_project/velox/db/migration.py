"""
Velox Framework - Database Migrations
"""
import json
from pathlib import Path
from velox.db.engine import db


class MigrationManager:
    def __init__(self, migrations_file='migrations.json'):
        self.migrations_file = migrations_file
        self.migrations = self._load_migrations()
    
    def _load_migrations(self):
        """Load migrations from file"""
        if Path(self.migrations_file).exists():
            with open(self.migrations_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_migrations(self):
        """Save migrations to file"""
        with open(self.migrations_file, 'w') as f:
            json.dump(self.migrations, f, indent=2)
    
    def make_migrations(self, app_name, models):
        """Create migration records for models"""
        if app_name not in self.migrations:
            self.migrations[app_name] = []
        
        migration = {
            'models': []
        }
        
        for model_cls in models:
            model_info = {
                'name': model_cls.__name__,
                'table': model_cls._table_name,
                'fields': {}
            }
            
            for field_name, field in model_cls._fields.items():
                model_info['fields'][field_name] = {
                    'type': field.field_type,
                    'primary_key': field.primary_key,
                    'unique': field.unique,
                    'auto_increment': field.auto_increment
                }
            
            migration['models'].append(model_info)
        
        self.migrations[app_name].append(migration)
        self._save_migrations()
        
        print(f"Created migrations for app '{app_name}'")
        return migration
    
    def migrate(self):
        """Apply all migrations"""
        db.connect()
        
        for app_name, app_migrations in self.migrations.items():
            print(f"Applying migrations for app '{app_name}'...")
            
            for migration in app_migrations:
                for model_info in migration['models']:
                    table_name = model_info['table']
                    fields = {}
                    
                    for field_name, field_def in model_info['fields'].items():
                        parts = [field_def['type']]
                        if field_def['primary_key']:
                            parts.append('PRIMARY KEY')
                        if field_def['auto_increment']:
                            parts.append('AUTOINCREMENT')
                        if field_def['unique'] and not field_def['primary_key']:
                            parts.append('UNIQUE')
                        
                        fields[field_name] = ' '.join(parts)
                    
                    db.create_table(table_name, fields)
                    print(f"  Created table '{table_name}'")
        
        print("Migrations applied successfully!")


# Global migration manager
migration_manager = MigrationManager()
