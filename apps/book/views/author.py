from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveDestroyAPIView, DestroyAPIView, RetrieveAPIView
from apps.book.models import Author
from apps.book.serializers import AuthorSerializer


# Function-based view
@api_view(['GET']) #by default, it uses a 'GET'
#@authentication_classes([BasicAuthentication])
@permission_classes ([IsAuthenticated])
def list_authors(request):
    authors = Author.objects.all()

    data = AuthorSerializer(authors, many = True)

    return Response(data.data, status = status.HTTP_200_OK)
"""
curl http://127.0.0.1:8000/api/v1/book/author/

curl -u admin:admin http://127.0.0.1:8000/api/v1/book/author/
"""
class DetailAuthor(RetrieveDestroyAPIView):
    # How do we handle generic views
    # ORM
    queryset = Author.objects.all()

    # Serializer
    serializer_class = AuthorSerializer

    # Authentication: Declar an authentication scheme to be used
    authentication_classes = (BasicAuthentication, )

    # Permissions: IsAuthenticated triggers the authentication process to take place
    permission_classes = (IsAuthenticated,)

class DeleteAuthor(DestroyAPIView):

    queryset = Author.objects.all()

    serializer_class = AuthorSerializer