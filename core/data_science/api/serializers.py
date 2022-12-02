from rest_framework import serializers   
from data_science.models import PlayerBio, Match, Season

class PlayerBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerBio
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'