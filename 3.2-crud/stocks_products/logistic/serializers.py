from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct
from django.db import transaction


class ProductSerializer(serializers.ModelSerializer):
   """
   Serializer таблице Product для представления ProductViewSet
   """
   class Meta:
       model = Product
       fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    """
    Дополнительный Serializer таблице StockProduct
    """
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
    


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    """
    Serializer таблице Stock с переопределение метотод create и update для возможности сделать 
    одним запросом запись в 2 таблицая Stock и StockProduct
    """
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions' ]

    @transaction.atomic
    def create(self, validated_data):
        positions = validated_data.pop('positions', [])
        stock = super().create(validated_data)
        StockProduct.objects.bulk_create([StockProduct(stock=stock, **position)for position in positions])
        return stock

    @transaction.atomic
    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for element in positions:
            created = StockProduct.objects.update_or_create(
                stock=stock,
                product=element['product'],
                defaults={'stock': stock, 'product': element['product'], 'quantity': element['quantity'], 'price': element['price']}
            )
        return stock