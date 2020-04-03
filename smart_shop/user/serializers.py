from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User
from django.conf import settings

from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager

# LOGIN--------------------------------------------------------------------------
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(
        required=True, 
        write_only=True,
        label="Password",
        style={'input_type': 'password'})


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields= ('id','email','name','is_staff','is_superuser','is_active','last_login','data_joined','auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self,obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass



# REGISTER--------------------------------------------------------------------------

# class UserRegisterSerializer(serializers.ModelSerializer):
#     """registering the user"""

#     class Meta:
#         model = User
#         fields = ('id','email' ,'name','password')

#     def validate_email(self, value):
#         user = User.objects.filter(email=value)
#         if user:
#             raise serializers.ValidationError("Email is already taken")
#         return BaseUserManager.normalize_email(value)

#     def validate_password(self, value):
#         password_validation.validate_password(value)
#         return value

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    # password_2 = serializers.CharField(
    #     required=True,
    #     label="Confirm Password",
    #     style={'input_type': 'password'}
    # )

    name = serializers.CharField(
        required=True
    )

    class Meta(object):
        model = User
        fields = ['id', 'email', 'password', 'name']
        # fields = ['id', 'email', 'password', 'password_2', 'name']
         

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    # def validate_password_2(self, value):
    #     data = self.get_initial()
    #     password = data.get('password')
    #     if password != value:
    #         raise serializers.ValidationError("Passwords doesn't match.")
    #     return value

# CHANGE PASSWORD ------------------------------------------------------------------


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value