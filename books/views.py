from rest_framework import viewsets, generics, permissions
from .models import Book, Category, Customer
from books import serializers, paginators


# Create your views here.
class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = paginators.BookPaginator
    permission_classes = [permissions.AllowAny]


class CustomerAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    pagination_class = paginators.BookPaginator
    permission_classes = [permissions.AllowAny]
