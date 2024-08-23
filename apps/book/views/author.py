from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Author
from apps.book.serializers import AuthorSerializer


# Function-based view
@api_view(['GET']) #by default, it uses a 'GET'
def list_authors(request):
    authors = Author.objects.all()

    data = AuthorSerializer(authors, many = True)

    return Response(data.data, status = status.HTTP_200_OK)
