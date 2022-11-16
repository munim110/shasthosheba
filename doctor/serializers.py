from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class DoctorSerializer(ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['user', 'designation', 'institute', 'phone', 'address', 'speciality', 'experience', 'image']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        doctor, created = Doctor.objects.update_or_create(user=user, designation=validated_data.pop('designation'),
         phone=validated_data.pop('phone'), institute=validated_data.pop('institute'))
        return doctor