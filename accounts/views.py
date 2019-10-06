from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import authentication, permissions
from .serializers import UserCreateSerializer, ProfileSerializer

# Create your views here.
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

#Profile
class ProfileDetails(RetrieveAPIView):
	serializer_class = ProfileSerializer

	def get_object(self):
		return self.request.user.profile


