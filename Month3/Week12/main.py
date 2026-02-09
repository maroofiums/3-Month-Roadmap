from velox import VeloxApp, json
from velox.models import VeloxBase
from sqlmodel import Field, SQLModel

app = VeloxApp()

# User table
class User(VeloxBase, table=True):
    name: str
    age: int

@app.route("/create_user")
async def create_user(request):
    data = {"name": "Maroof", "age": 18}
    user = await app.crud.create(User, data)
    return json({"id": user.id, "name": user.name})

@app.route("/get_user/<user_id:int>")
async def get_user(request, user_id):
    user = await app.crud.get(User, user_id)
    if not user:
        return json({"error": "User not found"}, status=404)
    return json({"id": user.id, "name": user.name})

if __name__ == "__main__":
    app.run()
