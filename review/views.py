from django.shortcuts import render
from .models import Like, Rating, Comment
from .serializers import CommentSerializer, RatingSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
