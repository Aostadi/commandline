import redis
import requests

# اتصال به Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# دریافت داده‌ها از یک API فرضی
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# ذخیره داده‌ها در Redis با استفاده از HSET
for item in data:
    post_id = item['id']
    client.hset(f"post:{post_id}", mapping={
        'userId': item['userId'],
        'title': item['title'],
        'body': item['body']
    })
print("Data stored in Redis")

# بازیابی و نمایش داده‌ها از Redis
for item in data:
    post_id = item['id']
    post_data = client.hgetall(f"post:{post_id}")
    # post_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in post_data.items()}
    # اگر از decode_responses=True استفاده کرده‌اید، نیازی به decode کردن مجدد نیست
    print(f"Post ID: {post_id}, Data: {post_data}")
