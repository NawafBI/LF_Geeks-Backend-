from .models import Game
from accounts.models import Profile
from accounts.serializers import ProfileLFGSerializer
from guilds.serializers import GuildNameSerializer
from guilds.models import Guild
from rest_framework import serializers

# TO View detail of game


class GameDetailSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()
    guilds = serializers.SerializerMethodField()
    # players change to players

    class Meta:
        model = Game
        fields = ["name", "year", "image", "genre",
                  "developer", "description", "players", "guilds"]

    def get_players(self, obj):
        players = Profile.objects.filter(games=obj)
        return ProfileLFGSerializer(players, many=True).data

    def get_guilds(self, obj):
        guilds = Guild.objects.filter(games=obj)
        return GuildNameSerializer(guilds, many=True).data


# TO CREATE GAME


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name", "year", "image",
                  "genre", "developer", "description"]


# TO GET GAME
class GetGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name", "year", "genre", "image"]
