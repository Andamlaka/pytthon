from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LoginView
from .views import RegisterView
from . import views

urlpatterns = [
    # Home page route
    path('', PostListView.as_view(), name='home'),
    
    # Blog post related routes
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/comment/edit/<int:comment_pk>/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('post/<int:pk>/comment/delete/<int:comment_pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('login/', LoginView.as_view(), name='login'),
    
    # Register route
    path('register/', RegisterView.as_view(), name='register'),
]
