import time
from concurrent import futures

import grpc

import books_pb2
import books_pb2_grpc

books_db = {}


class BookService(books_pb2_grpc.BookServiceServicer):
    def AddBook(self, request, context):
        books_db[request.id] = {
            'title': request.title,
            'author': request.author
        }
        return books_pb2.BookResponse(id=request.id, title=request.title, author=request.author)

    def GetBook(self, request, context):
        book = books_db.get(request.id)
        if book:
            return books_pb2.BookResponse(id=request.id, title=book['title'], author=book['author'])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found')
            return books_pb2.BookResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
