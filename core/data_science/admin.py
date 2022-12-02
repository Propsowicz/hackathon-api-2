from django.contrib import admin
from .models import PlayerBio, Match, Season

# Register your models here.

admin.site.register(PlayerBio)
# admin.site.register(Season)
admin.site.register(Season)
admin.site.register(Match)