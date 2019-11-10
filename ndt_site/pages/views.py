from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, 'pages/contact.html')


def accessories(request):
    return render(request, 'pages/accessories.html')


def biminis(request):
    return render(request, 'pages/biminis.html')


def installation(request):
    return render(request, 'pages/installation.html')


def faq(request):
    return render(request, 'pages/faq.html')

    