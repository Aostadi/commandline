from peewee import *

# تنظیمات پایگاه داده (اینجا از SQLite استفاده می‌شود)
db = SqliteDatabase('example.db')


# تعریف مدل‌ها
class BaseModel(Model):
    class Meta:
        database = db


class Department(BaseModel):
    name = CharField()
    size = IntegerField()


class Employee(BaseModel):
    name = CharField()
    department = ForeignKeyField(Department, backref='employees')


# ایجاد جدول‌ها
db.connect()
db.create_tables([Department, Employee])

# اضافه کردن برخی از داده‌ها برای مثال
dept1 = Department.create(name='HR', size=10)
dept2 = Department.create(name='Engineering', size=50)
dept3 = Department.create(name='Marketing', size=20)

Employee.create(name='Alice', department=dept1)
Employee.create(name='Bob', department=dept2)
Employee.create(name='Charlie', department=dept2)
Employee.create(name='David', department=dept3)

# Subquery برای یافتن بزرگترین دپارتمان
subquery = Department.select(Department.id).order_by(Department.size.desc()).limit(1)

# استفاده از Subquery در پرس و جوی اصلی
query = Employee.select().where(Employee.department.in_(subquery))

# نمایش نتایج
for employee in query:
    print(f'Employee Name: {employee.name}')
