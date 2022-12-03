from django.shortcuts import render
from .db_generator import createGenericPlayer

# Create your views here.

def create_player(request, *args, **kwargs):

    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        position = request.POST.get('position')
        nation = request.POST.get('nation')
        club = request.POST.get('club')
        foot = request.POST.get('foot')

    try:
        createGenericPlayer(f_name, l_name, position, nation, club, foot)
    except:
        print('error')

    return render(request, 'create_player.html', {'some': 'data'})
