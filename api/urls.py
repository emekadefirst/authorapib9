from django.urls import path
from .views import author_list, author_create, get_author, delete_author, update_author


urlpatterns = [    
    path('authors/', author_list, name='author-list'),
    path('authors/create/', author_create, name='author-create'),
    path('authors/<int:id>/', get_author, name='get-author'),
    path('authors/delete/<int:id>', delete_author, name='delete-author'),
    path('authors/update/<int:id>', update_author, name='update-author'),
]

