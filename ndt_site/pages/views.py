from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")


def contact(request):
    pass


def accessories(request):
    pass


def towers(request):
    pass


def biminis(request):
    pass


def blog(request):
    pass
    