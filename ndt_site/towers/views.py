from django.shortcuts import render
from .models import Towers
from .forms import SearchForm

# Create your views here.
def index(request):

    # query = request.GET.get('tower_id')
    form = SearchForm()
    
    towers = Towers.objects.values('title', 'description', 'price')
    images = Towers.objects.all()

    context = {
        'towers': towers,
        'images': images,
        'form': form
    }

    return render(request, 'towers/towers.html', context)




def tower(request, tower_id):

    
    form = SearchForm()
    print(tower_id)
    towers = Towers.objects.values('title', 'description', 'price')
    images = Towers.objects.all()

    context = {
        'towers': towers,
        'images': images,
        'form': form
    }

    return render(request, 'towers/towers.html', context)

