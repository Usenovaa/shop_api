from django.urls import path,include
from .views import CommentView, CommentDetailView, RatingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('rating', RatingViewSet)

urlpatterns = [
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
    path('',include(router.urls)),
]