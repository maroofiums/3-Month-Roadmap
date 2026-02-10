from sanic import Sanic
from sanic.response import json as sanic_json

class VeloxApp:
    def __init__(self):
        self._app = Sanic("VeloxApp")

        @self._app.get("/ping")
        async def ping(request):
            return sanic_json({"status": "pong"})

        @self._app.get("/health")
        async def health(request):
            return sanic_json({"status": "ok"})

    def route(self, path):
        def decorator(func):
            async def handler(request):
                result = func()
                return sanic_json(result)

            self._app.add_route(
                handler,
                path,
                methods=["GET"],
                name=f"route_{path}"
            )
            return func
        return decorator

    def run(self, host="0.0.0.0", port=8000):
        self._app.run(host=host, port=port, single_process=True)
