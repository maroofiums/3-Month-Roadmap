"""
Velox Framework - Response Objects
"""
import json


class JsonResponse:
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code
        self.content = json.dumps(data)
    
    def __repr__(self):
        return f'<JsonResponse status={self.status_code}>'
