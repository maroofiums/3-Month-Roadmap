#!/usr/bin/env python3
"""
Test script for Velox framework
"""
import sys
import os
import time
import json
from http.client import HTTPConnection
from threading import Thread

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_api():
    """Test the API endpoints"""
    time.sleep(2)  # Wait for server to start
    
    conn = HTTPConnection('127.0.0.1', 8000)
    
    print("\n=== Testing Velox API ===\n")
    
    # Test 1: GET /hello
    print("1. Testing GET /hello")
    conn.request('GET', '/hello')
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert data['message'] == "Hello from Users app!"
    print("   ✓ Passed\n")
    
    # Test 2: POST /users (create user)
    print("2. Testing POST /users (create user)")
    body = json.dumps({"name": "Alice", "email": "alice@example.com"})
    headers = {'Content-Type': 'application/json'}
    conn.request('POST', '/users', body, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert response.status == 201
    assert data['user']['name'] == "Alice"
    user_id = data['user']['id']
    print("   ✓ Passed\n")
    
    # Test 3: GET /users (list users)
    print("3. Testing GET /users (list users)")
    conn.request('GET', '/users')
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert len(data['users']) >= 1
    print("   ✓ Passed\n")
    
    # Test 4: GET /users/<id> (get specific user)
    print(f"4. Testing GET /users/{user_id} (get specific user)")
    conn.request('GET', f'/users/{user_id}')
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert data['user']['id'] == user_id
    print("   ✓ Passed\n")
    
    # Test 5: PUT /users/<id> (update user)
    print(f"5. Testing PUT /users/{user_id} (update user)")
    body = json.dumps({"name": "Alice Updated"})
    conn.request('PUT', f'/users/{user_id}', body, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert data['user']['name'] == "Alice Updated"
    print("   ✓ Passed\n")
    
    # Test 6: DELETE /users/<id> (delete user)
    print(f"6. Testing DELETE /users/{user_id} (delete user)")
    conn.request('DELETE', f'/users/{user_id}')
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    print(f"   Status: {response.status}")
    print(f"   Response: {data}")
    assert data['message'] == "User deleted successfully"
    print("   ✓ Passed\n")
    
    conn.close()
    
    print("=== All tests passed! ===\n")
    
    # Stop the server
    os._exit(0)


if __name__ == '__main__':
    # Change to demo directory and add to path
    demo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'demo')
    os.chdir(demo_path)
    sys.path.insert(0, demo_path)
    
    # Start the test in a separate thread
    test_thread = Thread(target=test_api, daemon=True)
    test_thread.start()
    
    # Import and run the server
    from velox.core import VeloxApp
    from velox.db import db
    
    app = VeloxApp('demo')
    
    from apps import users
    app.add_app(users)
    
    db.connect()
    
    # Run migrations
    from velox.db.migration import migration_manager
    migration_manager.migrate()
    
    print("\nStarting Velox server for testing...\n")
    app.run(host='127.0.0.1', port=8000)
