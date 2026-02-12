"""
Velox Framework - Database Engine
"""
import sqlite3
import json
from pathlib import Path


class DatabaseEngine:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path
        self.connection = None
    
    def connect(self):
        """Connect to the database"""
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        return self.connection
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
    
    def execute(self, query, params=None):
        """Execute a query"""
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor
    
    def fetchall(self, query, params=None):
        """Fetch all results from a query"""
        cursor = self.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def fetchone(self, query, params=None):
        """Fetch one result from a query"""
        cursor = self.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def create_table(self, table_name, fields):
        """Create a table from field definitions"""
        field_defs = []
        for field_name, field_type in fields.items():
            field_defs.append(f"{field_name} {field_type}")
        
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(field_defs)})"
        self.execute(query)
    
    def insert(self, table_name, data):
        """Insert a row into a table"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor = self.execute(query, tuple(data.values()))
        return cursor.lastrowid
    
    def update(self, table_name, data, condition, condition_params):
        """Update rows in a table"""
        set_clause = ', '.join([f"{k} = ?" for k in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        params = tuple(data.values()) + condition_params
        cursor = self.execute(query, params)
        return cursor.rowcount
    
    def delete(self, table_name, condition, condition_params):
        """Delete rows from a table"""
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor = self.execute(query, condition_params)
        return cursor.rowcount


# Global database instance
db = DatabaseEngine()
