from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from product.models import Product,Category
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import action
from review.serializers import LikeSerializer
from review.models import Like
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['price']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        product = self.get_object()
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author = serializer.validated_data.get('author'))
                like.delete()
                # like.is_liked = not like.is_liked
                # like.save()
                message = 'disliked'
            except Like.DoesNotExist:
                Like.objects.create(product=product, is_liked=True, author=serializer.validated_data.get('author'))
                message = 'liked'
            return Response(message, status=200)

