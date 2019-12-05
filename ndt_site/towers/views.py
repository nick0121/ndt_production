from django.shortcuts import render
from .models import Towers, Images
from .forms import SearchForm

# Create your views here.
################################# From index page no link parameter ############# Load all towers
def index(request):

    form = SearchForm()
    if request.method == "POST":
        selection = request.POST.get('tower_id')
        towers = Towers.objects.filter(manufacturer=selection)
    else:
        towers = Towers.objects.all()
    
    images = Images.objects.all()


    context = {
        'towers': towers,
        'form': form,
        'images': images,
    }

    return render(request, 'towers/towers.html', context)




#################################################### Render from Index manufacturer selection passes tower_id to method
def tower(request, tower_id):

    form = SearchForm()

    towers = Towers.objects.filter(manufacturer=tower_id)

    images = Images.objects.all()
    
    context = {
        'towers': towers,
        'form': form,
        'images': images,
    }

    return render(request, 'towers/towers.html', context)




########################################################## Render template from selection routes through select_tower
# def tower_from_select(request, manufacturer):
    
#     form = SearchForm()
#     if request.method == "POST":
#         selection = request.POST.get('tower_id')
#         towers = Towers.objects.filter(manufacturer=selection)
#     else:
#         towers = Towers.objects.all()
    
#     context = {
#         'towers': towers,
#         'form': form,
#     }

#     return render(request, 'towers/towers.html', context)