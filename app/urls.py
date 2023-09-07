from django.urls import path
from .views import GetAllPostView,CreatePostView,GetSinglePostView

urlpatterns = [
    path('posts/', GetAllPostView.as_view(), name='get_posts_list'),
    path('posts_data/', CreatePostView.as_view(), name='create_posts'),
    path('posts/<int:pk>/', GetSinglePostView.as_view(), name='get_single_post'),
]
