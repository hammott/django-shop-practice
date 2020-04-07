from django.shortcuts import render

from .models import User
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from . import serializers
from .utils import get_and_authenticate_user, create_user_account

# For Swagger 
from rest_framework.schemas import AutoSchema
import coreapi


# For Swagger API
# class UserViewSchema(AutoSchema):
#     def get_manual_fields(self,path,method):
#         extra_fields = []
#         if method.lower() in ['post','put']:
#             extra_fields = [
#                 coreapi.Field('email')
#             ]
#         manual_fields = super().get_manual_fields(path,method)
#         return manual_fields + extra_fields
    




# LOGIN REGISTER LOUGOUT CHANGE PASSWORD-------------------------------------------------------------------
class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login':serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }
    
    @action(methods=['POST',],detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response ({'error': 'Please provide both email and password'},
                                    status=status.HTTP_400_BAD_REQUEST)
        user = get_and_authenticate_user(**serializer.validated_data)
        if not user:
            return Response ({'error': 'Invalid Credentials'},
                                    status=status.HTTP_404_NOT_FOUND)

        # token, _ = Token.objects.get_or_create(user=user)
        # return Response({'token': token.key,'name':name},
        #             status=status.HTTP_200_OK)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST',],detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        # token, _ = Token.objects.get_or_create(user=user)
        # return Response({'token': token.key},
        #             status=status.HTTP_201_CREATED)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()




