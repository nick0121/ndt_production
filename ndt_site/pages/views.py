from django.shortcuts import render
from .forms import ContactForm


############################################################# INDEX VIEWS ############################################
def index(request):
    return render(request, "pages/index.html")
############################################################# ABOUT VIEWS ############################################
def about(request):
    return render(request, "pages/about.html")

############################################################# CONTACT VIEWS ############################################
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        'form': form,
    } 
    return render(request, 'pages/contact.html', context)


############################################################# ACCESSORIES VIEWS ############################################
def accessories(request):
    return render(request, 'pages/accessories.html')

############################################################# BIMINIS VIEWS ############################################
def biminis(request):
    return render(request, 'pages/biminis.html')

############################################################# INSTALLATION VIEWS ############################################
def installation(request):
    return render(request, 'pages/installation.html')

############################################################# FAQ VIEWS ############################################
def faq(request):
    return render(request, 'pages/faq.html')

    