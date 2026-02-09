from sanic import Sanic
from velox.routing import Router
from velox.db import VeloxDB
from velox.crud import VeloxCRUD

class VeloxApp:
    def __init__(self, name="VeloxApp"):
        self._sanic = Sanic(name)
        self.router = Router(self._sanic)
        self.db = VeloxDB()
        self.crud = VeloxCRUD(self.db)

    def route(self, path, methods=["GET"]):
        return self.router.route(path, methods)

    def run(self, host="0.0.0.0", port=8000, debug=True):
        import asyncio
        asyncio.run(self.db.init_db())
        self._sanic.run(host=host, port=port, debug=debug, single_process=True)
