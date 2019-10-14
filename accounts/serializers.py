from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password",
                  "first_name", "last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        profile = Profile.objects.get(user=new_user)
        print(self.context['request'].data['country'])
        profile.country = self.context['request'].data['country']
        profile.age = self.context['request'].data['age']
        profile.save()

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        # payload = jwt_payload_handler(new_user)
        # token = jwt_encode_handler(payload)

        # validated_data["token"] = token
        return validated_data

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError("Email Exists.")
        return email


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSeralizer()

    class Meta:
        model = Profile
        fields = ['user']

    # LFG=Looking for group


class ProfileLFGSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['username', 'image', 'cv', 'country']

    def get_username(self, obj):
        return "%s" % (obj.user.username)
