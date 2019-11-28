from django.shortcuts import render
from .models import Towers, Images, MANUFACTURERS

# Create your views here.
def index(request):

    towers = Towers.objects.all() ########## ADD SORT BY ############
    images = Images.objects.all()

    context = {
        'towers': towers,
        'images': images,
        'manufacturers': MANUFACTURERS,
    }

    return render(request, 'towers/towers.html', context)


def tower(request):
    return render(request, 'towers/tower.html')

