from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="towers"),
    path('<slug:tower_id>/', views.tower, name="tower"),
]
