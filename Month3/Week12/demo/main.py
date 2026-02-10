from velox import VeloxApp

app = VeloxApp()

@app.route("/hello")
def hello():
    return {"msg": "Hello Velox"}

app.run()
