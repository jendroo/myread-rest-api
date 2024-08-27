from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializers import TagSerializer


# Function-based view
@api_view(['GET']) #by default, it uses a 'GET'
def list_tags(request): #JSON Parser
    tags = Tag.objects.all() #Complex Data type

    #Deserialization
    data = TagSerializer(tags, many = True) # Convert complex data type to primitive python

    return Response(data.data, status = status.HTTP_200_OK)
