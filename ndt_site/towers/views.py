from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'towers/towers.html')


def tower(request):
    return render(request, 'towers/tower.html')

