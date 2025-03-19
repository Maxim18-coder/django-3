from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review  # Убедитесь, что модель Review определена
        fields = ['product', 'text', 'mark', 'created_at']


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']
    # реализуйте поля title, description, price и reviews (список отзывов к товару)