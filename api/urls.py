from django.urls import path
from .views import (
    author_list, 
    author_create, 
    get_author, 
    delete_author, 
    update_author, 
    CategoryListCreateAPIView, 
    CategoryRUDAPIView,
    BookListCreateAPIView,
    BookRUDAPIView
)


urlpatterns = [    
    path('authors/', author_list, name='author-list'),
    path('authors/create/', author_create, name='author-create'),
    path('authors/<int:id>/', get_author, name='get-author'),
    path('authors/delete/<int:id>', delete_author, name='delete-author'),
    path('authors/update/<int:id>', update_author, name='update-author'),
   
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryRUDAPIView.as_view(), name='category-rud'),


    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:id>/', BookRUDAPIView.as_view(), name='book-rud'),
]

