from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializers import TagSerializer


# Function-based view
@api_view(['GET']) #by default, it uses a 'GET'
def list_tags(request):
    tags = Tag.objects.all()

    data = TagSerializer(tags, many = True)

    return Response(data.data, status = status.HTTP_200_OK)
