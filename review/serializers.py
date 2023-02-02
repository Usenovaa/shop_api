from rest_framework import serializers
from .models import Like, Rating, Comment


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if  0 > rating > 5:
            raise serializers.ValidationError(
                'rating must be beetween 0 and 5'
            )
        return rating

class LikeSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'



    
