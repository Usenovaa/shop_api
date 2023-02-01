from rest_framework.serializers \
    import ModelSerializer
from rest_framework import serializers
from .models import Product, Category
from review.serializers import RatingSerializer
from review.models import Rating

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError(
                'Цена не может быть отрицательной'
            )
        return price

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ratings'] = RatingSerializer(
            instance.ratings.all(), many=True).data
        return representation

