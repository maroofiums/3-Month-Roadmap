from fastapi import FastAPI
from pydantic import BaseModel
import redis
import json

app = FastAPI()

r = redis.Redis(host='localhost',port=6379,decode_responses=True)

class NotificationRequest(BaseModel):
    user_id:int
    type: str
    message: str

@app.post("/notify")
def send_notification(request:NotificationRequest):
    notification = {
        "user_id":request.user_id,
        "type":request.type,
        "message":request.message
    }

    r.lpush("notifications", json.dumps(notification))
    return {"message":"Notification sent","notification":notification}


