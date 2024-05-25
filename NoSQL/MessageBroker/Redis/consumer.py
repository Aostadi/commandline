import json

import redis

# اتصال به Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    # دریافت و پردازش داده‌ها از صف
    message = client.brpop(['data_queue'])
    if message:
        queue_name, message_content = message
        item = json.loads(message_content.decode('utf-8'))
        # پردازش داده‌ها
        print(f"Processing: {item['id']} - {item['title']}")
