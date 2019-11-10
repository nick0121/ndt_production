from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:blog_id>', views.blog, name="blog"),
    path('search', views.search, name="search"),
]