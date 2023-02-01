from django.shortcuts import render
from product.models import Product, Category
from rest_framework.viewsets \
    import ModelViewSet
from .serializers import CategorySerializer, \
    ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

