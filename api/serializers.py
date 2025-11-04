from rest_framework import serializers
from .models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_id', 'author', 'category', 'category_id', 'published_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


