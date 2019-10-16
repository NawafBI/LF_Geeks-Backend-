# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Guild, Question, Recruitment, Answer
#bulk framwork
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

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


#games detail list in games
class GuildNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ["name", "tag", "description"]


#Questions
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["title", "active", "guild"]

# create answers
class AnswerSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Answer
        fields = ["question", "answer"]
       
        list_serializer_class = BulkListSerializer

#recruitment 
class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = ["status"]








