from django.shortcuts import render
from .models import Categories, Events
# Create your views here.


def index(request):
    events = Events.objects.all()
    return render(request, 'events/index.html', {'events': events})


def categories(request):
    categories = Categories.objects.all()
    return render(request, 'events/categories.html', {'categories': categories})
