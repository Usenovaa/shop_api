from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('ratings', views.RatingViewSet)

urlpatterns = [
    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('', include(router.urls)),
]
