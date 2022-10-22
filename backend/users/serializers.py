from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter
from .models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MigrationProfileSerializer(BaseSerializer):
    def serialize(self):
        return repr(self.value), {}


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user', 'pfp_url', 'runs', 'balls', 'matches', 'innings', 'batting_innings', 'bowling_innings', 'wickets',
            'overs', 'bowling_runs')


MigrationWriter.register_serializer(Profile, MigrationProfileSerializer)
