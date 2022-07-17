from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import User


from client.serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def get(request):
    users = UserSerializer.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
