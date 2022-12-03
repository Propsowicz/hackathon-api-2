from django.shortcuts import render
from .db_generator import createGenericPlayer

# Create your views here.

def create_player(request, *args, **kwargs):
    createGenericPlayer('Robert', 'Wasilewski', 'LM', 'POL', 'Śląsk Wrocław', 'right')
    return render(request, 'create_player.html', {'some': 'data'})
