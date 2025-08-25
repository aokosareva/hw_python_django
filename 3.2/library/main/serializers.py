from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.orders.count()

        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        books = BookSerializer(instance.books, many=True)
        representation['books'] = books.data

        return representation
