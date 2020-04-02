from django.contrib.auth import authenticate, login
from rest_framework import serializers
from .models import User


# LOGIN------------------------------------------------------------------------
def get_and_authenticate_user(email,password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid Username or Password")
    return user




# REGISTER--------------------------------------------------------------------------
def create_user_account(email, password, name="", **extra_fields):
    user = User.objects.create_user(
                                email=email, 
                                password=password, 
                                name=name,
                                **extra_fields
                                )
    return user