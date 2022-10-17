from django.urls import path
from . import views

urlpatterns=[
    # we will define all app-level urls in this array
    path('', views.home, name='home'), # renders the home view for the root path
    path('about/', views.about, name='about'), # creates the about path on the main app
    path('cats/', views.cats_index, name='index'),

]