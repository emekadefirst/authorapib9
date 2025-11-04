from django.shortcuts import render
from .serializers import AuthorSerializer, Author
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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