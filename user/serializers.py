from rest_framework import serializers
from .models import User, Token
from django.db  import transaction


class UserregisterSerializer(serializers.Serializer):
    password1=serializers.CharField(write_only=True, required=True)
    password=serializers.CharField()
    username = serializers.CharField()
    
    
    
    
    class Meta:
        model = User
        fields = ("id", "username", "password", "password1")
        extra_kwargs = {
            'password' : {'username', 'password', 'password'},
        }
        
        
    def validate(self, attrs):
        res = super().validate(attrs)
        password1 = attrs.pop('password1')
        if attrs['password'] != password1:
            raise serializers.ValidationError("Passwordlar mos kelmadi")
        return attrs


    def create(self, validated_data):
        password = validated_data['password']
        with transaction.atomic():
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
           
            
        return user
    
    
class UserLoginSerializer(serializers.Serializer):
    token = serializers.SerializerMethodField()
    username = serializers.CharField()
    password = serializers.CharField()
    
    
    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.token
    
    def validate(self, attrs):
        user = self.Meta.model.objects.filter
        