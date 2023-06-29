from .models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    phone_number = serializers.CharField(max_length=11)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        
        username_exits= User.objects.filter(username=attrs['username']).exists()
        if username_exits:
            raise serializers.ValidationError(detail='Username already exits')
        
        email_exits= User.objects.filter(email=attrs['email']).exists()
        if email_exits:
            raise serializers.ValidationError(detail='Email already exits')
        
        phone_number_exits= User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phone_number_exits:
            raise serializers.ValidationError(detail='Phone number already exits')
                                              
        return super().validate(attrs)
