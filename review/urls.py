from django.urls import path
from .views import CommentView, CommentDetailView

urlpatterns = [
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]