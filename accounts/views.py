from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import authentication, permissions
from .serializers import UserCreateSerializer

# Create your views here.
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer