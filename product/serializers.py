from rest_framework import serializers

from django.db.models import Avg

from .models import Product, Category
from review.models import Rating
from review.serializers import RatingSerializer, CommentSerializer, LikeSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price cannot be lower than 0")
        return price

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ratings'] = RatingSerializer(instance.ratings.all(), many=True).data
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['likes'] = LikeSerializer(instance.likes.all(), many=True).data
        representation['likes'] = instance.likes.count()
        return representation
