from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PlayerBioSerializer, SeasonSerializer, MatchesSerializer
from data_science.models import PlayerBio, Season, Match
from .custom_serializers import total_stats, each_match_stats, correlations

import json

class PlayerBioAPI(APIView):

    def get(self, request, id):

        player_bio = PlayerBio.objects.get(id=id)
        serializer = PlayerBioSerializer(player_bio, many=False)

        return Response(serializer.data)

class PlayersBioAPI(APIView):

    def get(self, request):

        player_bio = PlayerBio.objects.all()
        serializer = PlayerBioSerializer(player_bio, many=True)

        return Response(serializer.data)

class PlayerStatsAPI(APIView):

    def get(self, request, id, season):
        season_changed = season.replace('-', '/')
        player = PlayerBio.objects.get(id=id)
        season = Season.objects.filter(player=player, name=season_changed)[0]
        matches = Match.objects.filter(season=season)
        serializer = MatchesSerializer(matches, many=True)
        

        # season = SeasonStats.objects.filter(player=player, name=season_changed)[0]
        # serializer = SeasonStatsSerializer(season, many=False)

        return Response(serializer.data)


class PlayerTotalStatsAPI(APIView):

    def get(self, request, id, season):

        season_changed = season.replace('-', '/')
        player = PlayerBio.objects.get(id=id)
        season_id = Season.objects.filter(player=player, name=season_changed)[0].id
        correlations(season_id)

        return Response([ 
                        total_stats(season_id),         
                        ])

class PlayerDetailsAPI(APIView):

    def get(self, request, id, season):
        season_changed = season.replace('-', '/')
        player = PlayerBio.objects.get(id=id)
        season_id = Season.objects.filter(player=player, name=season_changed)[0].id
        correlations(season_id)

        return Response([correlations(season_id),
                        each_match_stats(season_id),                 
                        ])

