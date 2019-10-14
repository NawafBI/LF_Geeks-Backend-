from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import GuildSerializer, DetailSerializer, CreateSerializer, QuestionSerializer
from .models import Guild, Question

# Create your views here.


class GuildView(ModelViewSet):
    queryset = Guild.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return GuildSerializer
        if self.action == "detail":
            return DetailSerializer
        if self.action == "create":
            return CreateSerializer
        if self.action == "update":
            return DetailSerializer

    def perform_create(self, serializer):
        serializer.save(master=self.request.user.profile)


# create
class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionSerializer

# Questions


class QuestionsView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# update


class QuestionsUpdateView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
