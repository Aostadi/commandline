import json

import redis
import requests

# اتصال به Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# دریافت داده‌ها از یک API فرضی
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# ارسال داده‌ها به صف
for item in data:
    client.lpush('data_queue', json.dumps(item))
    print(f"Sent: {item['id']} - {item['title']}")
