from django.shortcuts import render
from .models import Games
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework import authentication, permissions
from .serializers import GameSerializer, GetGameSerializer

# Create your views here.
class GameCreateAPIView(CreateAPIView):
	serializer_class = GameSerializer


class GameView(ListAPIView):
	queryset = Games.objects.all()
	serializer_class = GetGameSerializer

	# def get_serializer_class(self):
	# 	if self.action == "list":
	# 		return GetGameSerializer
