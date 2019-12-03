from django.shortcuts import render
from .models import Towers
from .forms import SearchForm

# Create your views here.
def index(request):

    query = request.GET.get('tower_id')
    if query == None:
        query = 'mastercraft'

    form = SearchForm()
    
    towers = Towers.objects.filter(manufacturer=query)


    context = {
        'towers': towers,
        'form': form,
    }

    return render(request, 'towers/towers.html', context)




def tower(request, tower_id):

    
    form = SearchForm(tower_id)
    
    towers = Towers.objects.filter(manufacturer=tower_id)
    

    context = {
        'towers': towers,
        'form': form,
    }

    return render(request, 'towers/towers.html', context)

