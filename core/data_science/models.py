from django.db import models

class PlayerBio(models.Model):
    foot = [
        ('left', 'left'),
        ('right', 'right'),
        ('both', 'both')
    ]

    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    main_position = models.CharField(max_length=155, blank=True, null=True)
    nationality = models.CharField(max_length=155, blank=True, null=True)
    current_club = models.CharField(max_length=155, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    b_day = models.DateField()
    pref_foot = models.CharField(max_length=99, choices=foot)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Season(models.Model):
    player = models.ForeignKey(PlayerBio, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=9,blank=True, null=True)
    club = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.name} {self.player}'

class Match(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)

    oponnent_name = models.CharField(max_length=155)
    team_goals_scored = models.IntegerField(default=0)
    team_goals_lost = models.IntegerField(default=0)

    player_goals = models.IntegerField(default=0)
    player_assists = models.IntegerField(default=0)
    player_minutes = models.IntegerField(default=0)
    player_yellow_card = models.BooleanField(default=False)
    player_red_card = models.BooleanField(default=False)
  

    def __str__(self):
        return f'{self.season.club} : {self.oponnent_name}'

class DetailMatchStats(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, null=True, blank=True)

    # defensives
    tackles = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    fouls  = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0 )

    # offensives
    shots = models.IntegerField(default=0)
    key_passes = models.IntegerField(default=0)
    dribbles = models.IntegerField(default=0)
    fouled = models.IntegerField(default=0)
    offsides = models.IntegerField(default=0)

    # passes
    passes = models.IntegerField(default=0)
    passes_on_target = models.IntegerField(default=0)
    crosses = models.IntegerField(default=0)

    def __str__(self):
        return f'details of: {self.match.season.club} : {self.match.oponnent_name}'