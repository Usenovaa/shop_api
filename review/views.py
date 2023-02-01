from django.shortcuts import render
from .models import Like, Rating, Comment
from .serializers import CommentSerializer
from rest_framework import generics


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
