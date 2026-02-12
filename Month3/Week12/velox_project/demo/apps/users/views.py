"""
users app - Views
"""
from velox.core import JsonResponse
from apps.users.models import User


def register_routes(router):
    """Register app routes"""
    # CRUD endpoints
    router.add_route('GET', '/users', list_users)
    router.add_route('POST', '/users', create_user)
    router.add_route('GET', '/users/<id>', get_user)
    router.add_route('PUT', '/users/<id>', update_user)
    router.add_route('DELETE', '/users/<id>', delete_user)
    
    # Custom route
    router.add_route('GET', '/hello', hello)


def hello(request):
    """Custom hello endpoint"""
    return {"message": "Hello from Users app!"}


def list_users(request):
    """GET /users - List all users"""
    try:
        users = User.all()
        return JsonResponse({
            'users': [user.to_dict() for user in users]
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=500)


def create_user(request):
    """POST /users - Create a new user"""
    try:
        body = request.get('body', {})
        
        if not body:
            return JsonResponse({'error': 'Request body is required'}, status_code=400)
        
        name = body.get('name')
        email = body.get('email')
        
        if not name or not email:
            return JsonResponse({'error': 'name and email are required'}, status_code=400)
        
        # Check if email already exists
        existing_user = User.get(email=email)
        if existing_user:
            return JsonResponse({'error': 'Email already exists'}, status_code=400)
        
        # Create and save user
        user = User(name=name, email=email)
        user.save()
        
        return JsonResponse({
            'message': 'User created successfully',
            'user': user.to_dict()
        }, status_code=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=500)


def get_user(request):
    """GET /users/<id> - Get a single user"""
    try:
        user_id = request['params'].get('id')
        
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status_code=400)
        
        user = User.get(id=int(user_id))
        
        if not user:
            return JsonResponse({'error': 'User not found'}, status_code=404)
        
        return JsonResponse({
            'user': user.to_dict()
        })
    except ValueError:
        return JsonResponse({'error': 'Invalid user ID'}, status_code=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=500)


def update_user(request):
    """PUT /users/<id> - Update a user"""
    try:
        user_id = request['params'].get('id')
        body = request.get('body', {})
        
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status_code=400)
        
        if not body:
            return JsonResponse({'error': 'Request body is required'}, status_code=400)
        
        user = User.get(id=int(user_id))
        
        if not user:
            return JsonResponse({'error': 'User not found'}, status_code=404)
        
        # Update fields
        if 'name' in body:
            user.name = body['name']
        
        if 'email' in body:
            # Check if new email already exists (for other users)
            existing_user = User.get(email=body['email'])
            if existing_user and existing_user.id != user.id:
                return JsonResponse({'error': 'Email already exists'}, status_code=400)
            user.email = body['email']
        
        user.save()
        
        return JsonResponse({
            'message': 'User updated successfully',
            'user': user.to_dict()
        })
    except ValueError:
        return JsonResponse({'error': 'Invalid user ID'}, status_code=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=500)


def delete_user(request):
    """DELETE /users/<id> - Delete a user"""
    try:
        user_id = request['params'].get('id')
        
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status_code=400)
        
        user = User.get(id=int(user_id))
        
        if not user:
            return JsonResponse({'error': 'User not found'}, status_code=404)
        
        user.delete()
        
        return JsonResponse({
            'message': 'User deleted successfully'
        })
    except ValueError:
        return JsonResponse({'error': 'Invalid user ID'}, status_code=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status_code=500)
