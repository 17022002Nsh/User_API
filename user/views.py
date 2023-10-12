from django.shortcuts import render
from user.serializers import UserregisterSerializer
from rest_framework.response import Response
from .models import User , Token
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST



@api_view(['POST'])

def user_register(request, *args, **kwargs):
    serializer = UserregisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({ 'status' : True, 'data' : serializer.data })



@api_view(['POST', 'GET'])
def user_login(request, *args, **kwargs):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.filter(username=username).first()
    if not user or not user.check_password(password):
        return Response({
            "status" : False,
            'error': "User not found",
        }, status=HTTP_400_BAD_REQUEST)
    token, _ =Token.objects.get_or_create(user=user)
    return Response({
        "status" : True,
        "username" : username,
        "token" : token.token
    })
    
    

