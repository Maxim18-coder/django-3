from rest_framework import serializers
from sqlalchemy.ext.orderinglist import ordering_list

from .models import book, order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

    # доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.order_set.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation
