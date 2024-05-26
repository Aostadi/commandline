from peewee import *

db = SqliteDatabase('example.db')


class BaseModel(Model):
    class Meta:
        database = db


class Author(BaseModel):
    name = CharField()


class Book(BaseModel):
    title = CharField()
    author = ForeignKeyField(Author, backref='books')


db.connect()
db.create_tables([Author, Book])

# اضافه کردن داده‌ها
author1 = Author.create(name='Author 1')
Book.create(title='Book 1', author=author1)
Book.create(title='Book 2', author=author1)

# استفاده از select_related
query = Book.select().join(Author).select_related(Author)

for book in query:
    print(f'Book: {book.title}, Author: {book.author.name}')

# استفاده از prefetch
authors_with_books = Author.select().prefetch(Book)

for author in authors_with_books:
    print(f'Author: {author.name}')
    for book in author.books:
        print(f'  Book: {book.title}')
