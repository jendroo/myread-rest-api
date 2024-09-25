from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializers import TagSerializer

"""
curl http://127.0.0.1:8000/api/v1/book/tag/
token_header = 'Authentication: Token ea6fa5e750f1f9471653c339e93d53aed1b3fcc0'

curl -H 'Authorization: Token e482f80cadf5fc72db608413c019990a245ee4b0' http://127.0.0.1:8000/api/v1/book/author
"""

# Function-based view
@api_view(['GET']) #by default, it uses a 'GET'
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request): #JSON Parser
    tags = Tag.objects.all() #Complex Data type

    #Deserialization
    data = TagSerializer(tags, many = True) # Convert complex data type to primitive python

    return Response(data.data, status = status.HTTP_200_OK)
