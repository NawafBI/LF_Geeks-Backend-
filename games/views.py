from django.shortcuts import render
from .models import Game
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import authentication, permissions
from .serializers import GameSerializer, GetGameSerializer, GameDetailSerializer

# Create your views here.


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class GameCreateAPIView(CreateAPIView):
    serializer_class = GameSerializer


class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer

# the game detail must have a list of guilds and list of players
