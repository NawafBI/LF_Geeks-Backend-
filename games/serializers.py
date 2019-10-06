from .models import Games
from rest_framework import serializers

#TO CREATE GAME
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ["name", "year", "image", "genre", "developer", "description"]

# TO GET GAME
class GetGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ["name", "year", "genre", "image"]





