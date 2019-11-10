from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="towers"),
    path('<int:tower_id>', views.tower, name="tower"),
]