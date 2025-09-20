# accounts/jwt_serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Accept 'email' & 'password' as input (instead of 'username')
    """
    def validate(self, attrs):
        # attrs expected to have 'email' and 'password' from client
        email = attrs.get('email') or attrs.get('username')
        password = attrs.get('password')

        if email is None or password is None:
            raise AuthenticationFailed('Email and password required.')

        user = authenticate(username=email, password=password)
        if user is None:
            raise AuthenticationFailed('Invalid credentials.')

        # call parent with username/password so token pair is created
        data = super().validate({'username': user.username, 'password': password})
        # add user info
        data['user'] = {
            'id': user.id,
            'name': user.first_name,
            'email': user.email,
        }
        return data
