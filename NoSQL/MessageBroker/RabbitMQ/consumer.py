import json

import pika

# اتصال به RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# ایجاد یک صف
channel.queue_declare(queue='data_queue')


# تعریف یک تابع برای پردازش پیام‌ها
def callback(ch, method, properties, body):
    item = json.loads(body)
    # پردازش داده‌ها
    print(f"Processing: {item['id']} - {item['title']}")


# ثبت تابع callback برای دریافت پیام‌ها از صف
channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
