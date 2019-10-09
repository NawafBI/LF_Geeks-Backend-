from .models import Game
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from guilds.serializers import GuildNameSerializer
from guilds.models import Guild
from rest_framework import serializers

#TO View detail of game
class GameDetailSerializer(serializers.ModelSerializer):
	members = serializers.SerializerMethodField(),
	guilds = serializers.SerializerMethodField()
	class Meta:
		model = Game
		fields = ["name", "year", "image", "genre", "developer", "description", "members", "guilds"]

	def get_members(self, obj):
			members = Profile.objects.filter(games=obj)
			return ProfileSerializer(members, many=True).data

	def get_guilds(self, obj):
			guilds = Guild.objects.filter(games=obj)
			return GuildNameSerializer(guilds, many=True).data

#TO CREATE GAME
class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ["name", "year", "image", "genre", "developer", "description"]


# TO GET GAME
class GetGameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ["name", "year", "genre", "image"]





