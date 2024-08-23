from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from apps.book.models import Book, Author
from apps.book.serializers import ReadBookSerializer, CreateBookSerializer


# List book -> GET

@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()

    data = ReadBookSerializer(books, many = True)

    return Response(data.data, status = status.HTTP_200_OK)

# CREATE -> POST
@api_view(['POST'])
def create_book(request):
    with transaction.atomic():
        data = request.data #retrieve request body
        authors = data['authors']

        book = CreateBookSerializer(data=data)

        #if book.is_valid():
        book.is_valid()
        saved_book = book.save()

        for author in authors:
            author_obj = Author.objects.get(pk=author['id'])
            saved_book.authors.add(author_obj, through_defaults={'role':author['role']})
        
    return Response({'isbn':saved_book.isbn}, status=status.HTTP_201_CREATED)
    
    #return Response({'detail':'Invalid request data', 'error': 'Invalid_Request'}, status=status.HTTP_400_BAD_REQUEST)