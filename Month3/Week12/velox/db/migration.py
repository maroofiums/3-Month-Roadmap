import json
import os
from velox.db.engine import VeloxDB

def makemigrations(models):
    schema = {}
    for model in models:
        schema[model.__name__] = model._fields

    with open("migrations.json", "w") as f:
        json.dump(schema, f, indent=2)

def migrate():
    if not os.path.exists("migrations.json"):
        print("❌ No migrations found. Run `velox makemigrations` first.")
        return

    db = VeloxDB()
    schema = json.load(open("migrations.json"))

    for table, fields in schema.items():
        columns = ", ".join([f"{k} {v}" for k, v in fields.items()])
        sql = f"CREATE TABLE IF NOT EXISTS {table} ({columns})"
        db.execute(sql)

    print("✅ Migration complete")
