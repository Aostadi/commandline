from peewee import *

# تنظیمات پایگاه داده (اینجا از SQLite استفاده می‌شود)
db = SqliteDatabase('example.db')


# تعریف مدل‌ها
class BaseModel(Model):
    class Meta:
        database = db


class Department(BaseModel):
    name = CharField()


class Employee(BaseModel):
    name = CharField()
    department = ForeignKeyField(Department, backref='employees')


# ایجاد جدول‌ها
db.connect()
db.create_tables([Department, Employee])

# اضافه کردن برخی از داده‌ها برای مثال
dept1 = Department.create(name='HR')
dept2 = Department.create(name='Engineering')
dept3 = Department.create(name='Marketing')

Employee.create(name='Alice', department=dept1)
Employee.create(name='Bob', department=dept2)
Employee.create(name='Charlie', department=dept2)
Employee.create(name='David', department=dept3)

# انجام عملیات INNER JOIN در peewee
query = (Employee
         .select(Employee.name, Department.name.alias('department_name'))
         .join(Department, on=(Employee.department == Department.id)))

# نمایش نتایج
for employee in query:
    print(f'Employee Name: {employee.name}, Department Name: {employee.department_name}')
