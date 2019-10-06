from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import authentication, permissions
from .serializers import GameSerializer

# Create your views here.
class GameCreateAPIView(CreateAPIView):
	serializer_class = GameSerializer

# class GameCreateAPIView(CreateAPIView):
# 	serializer_class = GameSerializer
