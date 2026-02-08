from sanic import Sanic
from velox.routing import Router

class VeloxApp:
    def __init__(self, name="VeloxApp"):
        self._sanic = Sanic(name)
        self.router = Router(self._sanic)

    def route(self, path, methods=["GET"]):
        return self.router.route(path, methods)

    def run(self, host="0.0.0.0", port=8000, debug=True):
        self._sanic.run(
            host=host,
            port=port,
            debug=debug
        )
