from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('accessories', views.accessories, name="accessories"),
    path('biminis', views.biminis, name="biminis"),
    path('installation', views.installation, name="installation"),
    path('faq', views.faq, name="faq"),
    path('sitemap', views.sitemap, name="sitemap"),
]