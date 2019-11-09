from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('towers', views.towers, name="towers"),
    path('accessories', views.accessories, name="accessories"),
    path('blog', views.blog, name="blog"),
    path('biminis', views.biminis, name="biminis")
]