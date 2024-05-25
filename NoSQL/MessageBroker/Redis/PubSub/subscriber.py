import redis

# اتصال به Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# ایجاد مشترک و ثبت نام در کانال
pubsub = client.pubsub()
pubsub.subscribe('notifications')

print("Subscribed to 'notifications' channel")

# دریافت پیام‌ها از کانال
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received: {message['data'].decode('utf-8')}")
