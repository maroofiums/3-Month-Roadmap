import redis,json,time

r = redis.Redis(host='localhost',port=6379,decode_responses=True)

print("Notification Producer Started...")

while True:
    task = r.rpop("notifications")
    if task:
        data = json.loads(task)
        print(f"Processing notification for user {data['user_id']}: {data['type']} - {data['message']}")
        time.sleep(2)  
    else:
        print("No notifications to process. Waiting...")
        time.sleep(100)
