from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Order, Book
from main.serializers import BookSerializer, OrderSerializer, BookListSerializer


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)  # передайте данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True):  # если данные валидны
            serializer.save()
            return Response('Книга успешно создана')  # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
