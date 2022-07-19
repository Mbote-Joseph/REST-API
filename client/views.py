from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User


from client.serializers import UserSerializers

# Create your views here.
@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer= UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save

    
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    