from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        try:
            user.first_name = validated_data['first_name']
        except:
            pass
        try:
            user.last_name = validated_data['last_name']
        except:
            pass
        user.save()
        return user

class IntermediarySerializer(ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Intermediary
        fields = ['user', 'address', 'nid', 'dob']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        intermediary, created = Intermediary.objects.update_or_create(user=user, address=validated_data.pop('address'),
         nid=validated_data.pop('nid'), dob=validated_data.pop('dob'))  
        return intermediary

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()
        instance.address = validated_data.get('address', instance.address)
        instance.nid = validated_data.get('nid', instance.nid)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name','age','intermediary']
    

