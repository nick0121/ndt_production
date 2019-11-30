from django.shortcuts import render
from .models import Towers, Images, MANUFACTURERS

# Create your views here.
def index(request):

    towers = Towers.objects.all()
    # towers = Towers.objects.values('title', 'description', 'price') ########## ADD SORT BY ############
    # images = Images.objects.all()

    context = {
        'towers': towers,
        # 'manufacturers': MANUFACTURERS,
    }

    return render(request, 'towers/towers.html', context)


def tower(request):
    return render(request, 'towers/tower.html')

