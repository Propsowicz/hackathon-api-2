from django.urls import path
from data_science.models import PlayerBio
from .views import PlayerBioAPI, PlayerStatsAPI, PlayerTotalStatsAPI, PlayersBioAPI, PlayerDetailsAPI, FavouritesPlayersBioAPI

urlpatterns = [
    path('player-bio/<int:id>/', PlayerBioAPI.as_view()),
    path('players-bio/', PlayersBioAPI.as_view()),
    path('players-bio/<str:ids>/', FavouritesPlayersBioAPI.as_view()),
    path('player-stats/<int:id>/<str:season>/', PlayerStatsAPI.as_view()),
    path('player-detail-stats/<int:id>/<str:season>/', PlayerDetailsAPI.as_view()),
    path('player-total-stats/<int:id>/<str:season>/', PlayerTotalStatsAPI.as_view()),  
    ]