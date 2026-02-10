import os

def makeproject(name):
    os.makedirs(name)
    os.chdir(name)

    os.makedirs("apps")
    open("apps/__init__.py", "w").close()

    with open("main.py", "w") as f:
        f.write(
"""from velox import VeloxApp

app = VeloxApp()

@app.route("/hello")
def hello():
    return {"msg": "Hello Velox"}

app.run()
"""
        )
