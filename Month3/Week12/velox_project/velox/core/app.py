"""
Velox Framework - Core Application
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from velox.core.router import Router
from velox.core.response import JsonResponse


class VeloxApp:
    def __init__(self, name):
        self.name = name
        self.router = Router()
        self.installed_apps = []
        
    def add_app(self, app_module):
        """Register an app with the Velox application"""
        self.installed_apps.append(app_module)
        # Load routes from the app's views
        if hasattr(app_module, 'views'):
            views = app_module.views
            if hasattr(views, 'register_routes'):
                views.register_routes(self.router)
    
    def route(self, path, methods=None):
        """Decorator to register routes"""
        if methods is None:
            methods = ['GET']
        
        def decorator(func):
            for method in methods:
                self.router.add_route(method, path, func)
            return func
        return decorator
    
    def run(self, host='127.0.0.1', port=8000):
        """Start the HTTP server"""
        handler = self._create_handler()
        server = HTTPServer((host, port), handler)
        print(f"Velox server running on http://{host}:{port}")
        print(f"Installed apps: {[app.__name__ for app in self.installed_apps]}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            server.shutdown()
    
    def _create_handler(self):
        """Create HTTP request handler with access to app instance"""
        app = self
        
        class VeloxRequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self._handle_request('GET')
            
            def do_POST(self):
                self._handle_request('POST')
            
            def do_PUT(self):
                self._handle_request('PUT')
            
            def do_DELETE(self):
                self._handle_request('DELETE')
            
            def _handle_request(self, method):
                parsed_url = urlparse(self.path)
                path = parsed_url.path
                query_params = parse_qs(parsed_url.query)
                
                # Get request body for POST/PUT
                body = None
                if method in ['POST', 'PUT']:
                    content_length = int(self.headers.get('Content-Length', 0))
                    if content_length > 0:
                        body_bytes = self.rfile.read(content_length)
                        try:
                            body = json.loads(body_bytes.decode('utf-8'))
                        except:
                            body = {}
                
                # Find matching route
                handler, params = app.router.match(method, path)
                
                if handler:
                    try:
                        # Call handler with request context
                        request = {
                            'method': method,
                            'path': path,
                            'params': params,
                            'query': query_params,
                            'body': body
                        }
                        response = handler(request)
                        
                        # Handle JsonResponse objects
                        if isinstance(response, JsonResponse):
                            self.send_response(response.status_code)
                            self.send_header('Content-Type', 'application/json')
                            self.end_headers()
                            self.wfile.write(response.content.encode('utf-8'))
                        elif isinstance(response, dict):
                            self.send_response(200)
                            self.send_header('Content-Type', 'application/json')
                            self.end_headers()
                            self.wfile.write(json.dumps(response).encode('utf-8'))
                        else:
                            self.send_response(200)
                            self.send_header('Content-Type', 'text/plain')
                            self.end_headers()
                            self.wfile.write(str(response).encode('utf-8'))
                    except Exception as e:
                        self.send_response(500)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        error_response = {'error': str(e)}
                        self.wfile.write(json.dumps(error_response).encode('utf-8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    error_response = {'error': 'Not Found'}
                    self.wfile.write(json.dumps(error_response).encode('utf-8'))
            
            def log_message(self, format, *args):
                """Override to customize logging"""
                print(f"{self.address_string()} - {format % args}")
        
        return VeloxRequestHandler
