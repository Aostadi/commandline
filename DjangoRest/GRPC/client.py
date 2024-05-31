import grpc

import books_pb2
import books_pb2_grpc


def add_book(stub, book_id, title, author):
    response = stub.AddBook(books_pb2.BookRequest(id=book_id, title=title, author=author))
    print(f'Added Book: {response.id}, {response.title}, {response.author}')


def get_book(stub, book_id):
    try:
        response = stub.GetBook(books_pb2.BookIdRequest(id=book_id))
        print(f'Got Book: {response.id}, {response.title}, {response.author}')
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            print('Book not found')
        else:
            print(f'Error occurred: {e.details()}')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = books_pb2_grpc.BookServiceStub(channel)
        add_book(stub, 1, 'The Great Gatsby', 'F. Scott Fitzgerald')
        get_book(stub, 1)
        get_book(stub, 2)


if __name__ == '__main__':
    run()
