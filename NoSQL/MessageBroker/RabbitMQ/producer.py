import json

import pika
import requests

# اتصال به RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# ایجاد یک صف
channel.queue_declare(queue='data_queue')

# دریافت داده‌ها از یک API فرضی
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# ارسال داده‌ها به صف
for item in data:
    message = json.dumps(item)
    channel.basic_publish(exchange='', routing_key='data_queue', body=message)
    print(f"Sent: {item['id']} - {item['title']}")

# بستن اتصال
connection.close()
