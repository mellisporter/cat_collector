from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Create your views here.


def home(request):
    #this is where we return a response
    # in most cases we render a template
    # we will need some dara for that template in most cases
    # return HttpResponse('<h1>Hello</h1>') this is the old way
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('This is the about page.') # renders response on request to the about route
    return render(request, 'about.html')


# Add the Cat class & list and view function below the imports
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]


def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})