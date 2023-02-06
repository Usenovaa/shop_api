from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from review.models import Like
from review.serializers import LikeSerializer
from rest_framework.decorators import action
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser,AllowAny
# Create your views here.


class PermissioinMixin():
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy','create']:
            permissions = [IsAdminUser,]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]



class ProductViewset(PermissioinMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['price']

    @action(['POST'], detail=True) #detail false = для queryset
    def like(self, request, pk=None):
        product = self.get_object()
        author = request.user
        serializer = LikeSerializer(data=request.data) # в сериализатор передаем ДАТА. В аднном случае всегда реквест
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(product=product, author = author)
                like.delete()
                message = 'Dislike'
            except Like.DoesNotExist:
                Like.objects.create(product=product, is_liked=True, author = author)
                message = 'Like posted'
            return Response(message, status=200)
        

class CategoryViewSet(PermissioinMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    



