from peewee import *

# تنظیمات پایگاه داده (اینجا از SQLite استفاده می‌شود)
db = SqliteDatabase('example.db')


# تعریف مدل‌ها
class BaseModel(Model):
    class Meta:
        database = db


class Sales(BaseModel):
    product_id = IntegerField()
    amount = IntegerField()


# ایجاد جدول
db.connect()
db.create_tables([Sales])

# اضافه کردن برخی از داده‌ها برای مثال
Sales.create(product_id=1, amount=100)
Sales.create(product_id=1, amount=150)
Sales.create(product_id=2, amount=200)
Sales.create(product_id=2, amount=50)
Sales.create(product_id=3, amount=300)

# استفاده از دستور GROUP BY در peewee
query = (Sales
         .select(Sales.product_id, fn.SUM(Sales.amount).alias('total_sales'))
         .group_by(Sales.product_id))

# نمایش نتایج
for sale in query:
    print(f'Product ID: {sale.product_id}, Total Sales: {sale.total_sales}')
