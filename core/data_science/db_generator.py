from .models import PlayerBio, Season, Match, DetailMatchStats
from random import randint
import random
from datetime import date

def createGenericPlayer(first_name, last_name, main_position, nationality, current_club, pref_foot):
    oponnents = ['Miedź Legnica', 'Piast Gliwice', 'Pogoń Szczecin', 'Raków Częstochowa', 'Radomiak Radom',
        'Śląsk Wrocław', 'Warta Poznań', 'Widzew Łodź', 'Korona Kielce', 'Cracovia Kraków', 'Legia Warszawa',
        'Zagłębie Lubin', 'Jagiellonia Białystok', 'Lech Poznań', 'Lechia Gdańsk', 'Stal Mielec', 'Wisła Płock', 'ŁKS Łódź'
        ]
    oponnents.pop(oponnents.index(current_club))
    b_day = date(1994, 5, 17)
    height = randint(170, 200)
    weight = randint(70, 95)
    price = randint(100000, 1000000)

    player = PlayerBio.objects.create(
        first_name = first_name, last_name = last_name, main_position = main_position, nationality = nationality,
        current_club = current_club, pref_foot = pref_foot, price = price, b_day = b_day, weight = weight, height = height
    )

    season = Season.objects.create(player=player, name='2021/2022', club=current_club)

    j = len(oponnents) - 1
    for i in range(17):
        oponnent = oponnents[randint(0, j)]
        j -= 1
        oponnents.pop(oponnents.index(oponnent))

        team_goals_scored = randint(0, 5)
        team_goals_lost = randint(0, 5)
        player_goals = randint(0, 3)
        player_assists = randint(0, 2)
        player_minutes = randint(45, 90)
        player_yellow_card = random.choices([True, False], weights=(5, 95), k=1)
        if player_yellow_card == [False]:
            player_yellow_card = False
        else:
            player_yellow_card = True
        player_red_card = random.choices([True, False], weights=(5, 95), k=1)
        if player_red_card == [False]:
            player_red_card = False
        else:
            player_red_card = True

        match_ = Match.objects.create(season=season, oponnent_name=oponnent, team_goals_scored=team_goals_scored,
                team_goals_lost=team_goals_lost, player_goals=player_goals, player_assists=player_assists,
                player_minutes=player_minutes, player_yellow_card=player_yellow_card, player_red_card=player_red_card
        )
        tackles = randint(0, 6)
        interceptions = randint(0, 6)
        fouls = randint(0, 6)
        dribbled = randint(0, 6)
        shots = randint(0, 10)
        shots_on_target = randint(0, 6)
        dribbles = randint(0, 10)
        fouled = randint(0, 6)
        offsides = randint(0, 6)
        passes = randint(15, 90)
        passes_on_target = randint(15, 80)
        key_passes = randint(0, 8)

        details = DetailMatchStats.objects.create(match=match_, tackles=tackles, interceptions=interceptions, fouls=fouls,
        dribbled=dribbled, shots=shots, shots_on_target=shots_on_target, dribbles=dribbles, fouled=fouled, offsides=offsides, 
        passes=passes, passes_on_target=passes_on_target, key_passes=key_passes
        )
        


# createGenericPlayer('Taduesz', 'Piechna', 'ST', 'POL', 'Korona Kielce', 'right')