from django.urls import path
from . import views

urlpatterns=[
    # we will define all app-level urls in this array
    path('', views.home, name='home'), # renders the home view for the root path
    path('about/', views.about, name='about'), # creates the about path on the main app
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # new route used to show a form and create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    # Add the new routes below
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),

]