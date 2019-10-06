from .models import Games
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ["name", "year", "image", "genre", "developer", "description"]

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ["name", "year", "genre", "image"]



