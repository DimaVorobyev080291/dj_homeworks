from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductViewSet(ModelViewSet):
    """
    ViewSet с полныс CRUD функционалом для таблице Product с возможностью поиска по полям 
    title и description и упорядочивание данных по полю id
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['id']


class StockViewSet(ModelViewSet):
    """
    ViewSet с полныс CRUD функционалом для таблице Stok с возможностью поиска по полю products
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products']
