from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import GuildSerializer, DetailSerializer, CreateSerializer
from .models import Guild

# Create your views here.
class GuildView(ModelViewSet):
	queryset = Guild.objects.all()

	def get_serializer_class(self):
		if self.action == "list":
			return  GuildSerializer
		if self.action == "detail":
			return DetailSerializer
		if self.action == "create":
			return CreateSerializer
		if self.action == "update":
			return DetailSerializer


	def perform_create(self, serializer):
		serializer.save(master=self.request.user.profile)
	
