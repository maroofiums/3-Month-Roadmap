import redis,json,time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

while True:
    task = r.rpop("email_queue")
    if task:
        task_data = json.loads(task)
        print(f"Processing task: {task_data}")
        time.sleep(1)  
    else:
        time.sleep(1)