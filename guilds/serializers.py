# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Guild


class GuildSerializer(serializers.ModelSerializer):
    games = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Guild
        fields = ["name", "games", "platform", "tag"]


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ["name", "games", "tag", "description", "platform"]


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ["name", "games", "platform", "tag", "description"]


# games detail list in games
class GuildNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ["name", "tag", "description"]
