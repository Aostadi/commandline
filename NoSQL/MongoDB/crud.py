from pymongo import MongoClient

# اتصال به MongoDB
client = MongoClient('mongodb://localhost:27017/')

# انتخاب پایگاه‌داده و مجموعه (collection)
db = client.example_database
collection = db.example_collection

# عملیات Create
document = {"name": "Alice", "age": 25, "city": "New York"}
result = collection.insert_one(document)
print(f"Document inserted with _id: {result.inserted_id}")

# عملیات Read
query = {"name": "Alice"}
retrieved_document = collection.find_one(query)
print(f"Retrieved document: {retrieved_document}")

# عملیات Update
update_query = {"name": "Alice"}
new_values = {"$set": {"age": 26}}
collection.update_one(update_query, new_values)
updated_document = collection.find_one(query)
print(f"Updated document: {updated_document}")

# عملیات Delete
delete_query = {"name": "Alice"}
collection.delete_one(delete_query)
deleted_document = collection.find_one(query)
print(f"Deleted document: {deleted_document}")
