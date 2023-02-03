from .models import Like, Rating, Comment, LikeComment
from .serializers import CommentSerializer, RatingSerializer, LikeCommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


# class CommentView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        comment = self.get_object()
        serializer = LikeCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = LikeComment.objects.get(comment=comment, author = serializer.validated_data.get('author'))
                like.delete()
                message = 'disliked'
            except LikeComment.DoesNotExist:
                LikeComment.objects.create(comment=comment, is_liked=True, author=serializer.validated_data.get('author'))
                message = 'liked'
            return Response(message, status=200)


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
