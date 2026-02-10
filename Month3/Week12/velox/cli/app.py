import os

def makeapp(name):
    path = f"apps/{name}"
    os.makedirs(path, exist_ok=True)

    open(f"{path}/__init__.py", "w").close()

    with open(f"{path}/models.py", "w") as f:
        f.write("from velox import Model, Field\n")

    with open(f"{path}/views.py", "w") as f:
        f.write("# routes here\n")
