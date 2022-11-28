from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken

from .models import *
from .serializers import *

# Create your views here.
class IntermediaryViewSet(viewsets.ModelViewSet):
    queryset = Intermediary.objects.all()
    serializer_class = IntermediarySerializer


class UserObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        checkUser = User.objects.filter(username=username).exists()
        
        if not checkUser:
            return Response({'non_field_errors': 'User does not exist'})
        
        response = super(UserObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        userSerializer = UserSerializer(user)
        return Response({'token': token.key, 'user': userSerializer.data})


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

