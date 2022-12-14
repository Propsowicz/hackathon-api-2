from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PlayerBioSerializer, SeasonSerializer, MatchesSerializer
from data_science.models import PlayerBio, Season, Match
from .custom_serializers import total_stats, each_match_stats, correlations

import json

class PlayerBioAPI(APIView):
    def get(self, request, id):
        try:
            player_bio = PlayerBio.objects.get(id=id)
            serializer = PlayerBioSerializer(player_bio, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PlayersBioAPI(APIView):
    def get(self, request):
        try:
            player_bio = PlayerBio.objects.all()
            serializer = PlayerBioSerializer(player_bio, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FavouritesPlayersBioAPI(APIView):
    def get(self, request, ids):
        x = ids[4::]
        list_of_ids = [int(x.split(',')[i]) for i in range(len(x.split(',')))]
        try:
            player_bio = PlayerBio.objects.filter(id__in=list_of_ids)
            serializer = PlayerBioSerializer(player_bio, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND)


class PlayerStatsAPI(APIView):
    def get(self, request, id, season):
        try:
            season_changed = season.replace('-', '/')
            player = PlayerBio.objects.get(id=id)
            season = Season.objects.filter(player=player, name=season_changed)[0]
            matches = Match.objects.filter(season=season)
            serializer = MatchesSerializer(matches, many=True)         
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PlayerTotalStatsAPI(APIView):
    def get(self, request, id, season):
        try:
            season_changed = season.replace('-', '/')
            player = PlayerBio.objects.get(id=id)
            season_id = Season.objects.filter(player=player, name=season_changed)[0].id
            return Response(total_stats(season_id), status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PlayerDetailsAPI(APIView):

    def get(self, request, id, season):
        try:
            season_changed = season.replace('-', '/')
            player = PlayerBio.objects.get(id=id)
            season_id = Season.objects.filter(player=player, name=season_changed)[0].id
            return Response([correlations(season_id),
                            each_match_stats(season_id),                 
                            ], status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
