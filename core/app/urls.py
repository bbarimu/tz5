from django.urls import path, include

from .views import post_create, post_list, create_author, create_category,post_detail
urlpatterns = [
    path('posts/', post_list),
    path('posts/create/', post_create),
    path('author/create/', create_author),
    path('posts/<int:pk>/', post_detail),
    path('category/create/', create_category)
]
