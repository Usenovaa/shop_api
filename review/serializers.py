from .models import Comment, Like, Rating
from rest_framework import serializers


class CommentSerializer(
    serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(
    serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'