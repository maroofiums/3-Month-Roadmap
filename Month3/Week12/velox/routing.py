class Router:
    def __init__(self, sanic_app):
        self.app = sanic_app

    def route(self, path, methods=["GET"]):
        def decorator(func):
            route_name = f"{func.__module__}.{func.__name__}"

            async def wrapper(request, *args, **kwargs):
                return await func(request)

            self.app.add_route(
                wrapper,
                path,
                methods=methods,
                name=route_name  # 🔑 UNIQUE ROUTE NAME
            )
            return func
        return decorator
