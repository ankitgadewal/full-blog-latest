from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/new-post', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('search', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('post/cat/<int:pk>/', views.PostCategory.as_view(), name='post_by_category'),
]
