"""
Velox Framework - Router
"""
import re


class Router:
    def __init__(self):
        self.routes = {}
    
    def add_route(self, method, path, handler):
        """Add a route to the router"""
        if method not in self.routes:
            self.routes[method] = []
        
        # Convert path params like /users/<id> to regex pattern
        pattern = self._path_to_pattern(path)
        self.routes[method].append({
            'path': path,
            'pattern': pattern,
            'handler': handler
        })
    
    def _path_to_pattern(self, path):
        """Convert path with <param> to regex pattern"""
        # Replace <param> with named groups
        pattern = re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', path)
        return re.compile(f'^{pattern}$')
    
    def match(self, method, path):
        """Match a path to a handler"""
        if method not in self.routes:
            return None, {}
        
        for route in self.routes[method]:
            match = route['pattern'].match(path)
            if match:
                return route['handler'], match.groupdict()
        
        return None, {}
