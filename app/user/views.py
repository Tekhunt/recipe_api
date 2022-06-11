
"""
User API views
"""

from yaml import serialize
from rest_framework import generics

from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

