from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse

# Create your views here.
from main_app.models import Cat

from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import FeedingForm



def home(request):
    #this is where we return a response
    # in most cases we render a template
    # we will need some dara for that template in most cases
    # return HttpResponse('<h1>Hello</h1>') this is the old way
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('This is the about page.') # renders response on request to the about route
    return render(request, 'about.html')


# # Add the Cat class & list and view function below the imports
# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]


# def cats_index(request):
#     return render(request, 'cats/index.html', {'cats': cats})

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })


def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form= FeedingForm()
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': feeding_form })


def add_feeding(request, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)



class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'


class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

