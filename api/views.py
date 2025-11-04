from django.shortcuts import render
from .serializers import AuthorSerializer, Author, CategorySerializer, Category, BookSerializer, Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics


"""Function Based Views for Author Model CRUD Operations"""

@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all().order_by('-created_at', '-updated_at')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def author_create(request):
    try:
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_author(request, id):
    author = Author.objects.get(id=id)
    if author is None:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        if author is None:
            return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['PUT'])
def update_author(request, id):
    try:
        author = Author.objects.get(id=id)
        if author is None:
            return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    


"""Class Based Views for Category Model CRUD Operations"""


class CategoryListCreateAPIView(APIView):
    def get(self, request): ## naming a method get in a CBV makes it respond to GET requests
        categories = Category.objects.all().order_by('-created_at', '-updated_at')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request): ## naming a method post in a CBV makes it respond to POST requests
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CategoryRUDAPIView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        category = self.get_object(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        category = self.get_object(id)
        if not category:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Generic Class Based Views for Book  Model CRUD Operations"""


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-created_at', '-updated_at')
    serializer_class = BookSerializer

class BookRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'