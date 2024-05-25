import redis

# اتصال به Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# ارسال پیام‌ها به کانال
channel = 'notifications'
messages = ['Hello, World!', 'This is a test message.', 'Pub/Sub with Redis!']
for message in messages:
    client.publish(channel, message)
    print(f"Published: {message}")
