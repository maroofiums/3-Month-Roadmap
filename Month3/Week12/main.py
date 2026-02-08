from velox import VeloxApp, json

app = VeloxApp()

@app.route("/hello")
async def hello(request):
    return json({"message": "Hello from Velox 🚀"})

@app.route("/ping")
async def ping(request):
    return json({"status": "pong"})

@app.route("/health")
async def health(request):
    return json({
        "status": "ok",
        "service": "velox",
        "uptime": "running"
    })

if __name__ == "__main__":
    app.run()
