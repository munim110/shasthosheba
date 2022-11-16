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

class DoctorSerializer(ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['user', 'designation', 'institute', 'phone', 'address', 'speciality', 'experience', 'image']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        doctor, created = Doctor.objects.update_or_create(user=user, designation=validated_data.pop('designation'),
         phone=validated_data.pop('phone'), institute=validated_data.pop('institute'))
        return doctor

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()
        instance.designation = validated_data.get('designation', instance.designation)
        instance.institute = validated_data.get('institute', instance.institute)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.speciality = validated_data.get('speciality', instance.speciality)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

