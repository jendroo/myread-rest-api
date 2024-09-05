from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Reader
from apps.reader.serializer import ReaderSerializer

class Login(APIView):

    def post(self, request):
        # Extract creentials
        password = request.data.get('password')
        username = request.data.get('username')

        # Authenticate the user
        user: User | None = authenticate(
            username=username,
            password=password
        )

        # Generate token
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                             status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'error':'Invalid_Credential', 
                 'detail': 'Username or password is incorrect'},
                status=status.HTTP_404_NOT_FOUND)
        
@api_view()
def detail_reader(request,pk):
    reader = Reader.objects.get(user__id=pk)

    # data = {
    #     "id":reader.id,
    #     "user":{
    #         "user_id":reader.user.id,
    #         "username":reader.user.username
    #     }

    # }
    data = ReaderSerializer(reader)

    return Response({'data': data.data})