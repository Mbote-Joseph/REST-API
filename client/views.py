from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import User


from client.serializers import UserSerializers

# Create your views here.
@api_view(['GET'])
def getUser(request):
    users = UserSerializers.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)
    
