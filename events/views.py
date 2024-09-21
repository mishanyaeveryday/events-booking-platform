from django.shortcuts import render
from .models import Categories, Events
# Create your views here.


def index(request):
    events = Events.objects.all()
    categories = Categories.objects.all()
    context = {
        'events': events,
        'categories': categories
    }
    return render(request, 'events/index.html', context)


def categories(request):
    categories = Categories.objects.all()
    return render(request, 'events/categories.html', {'categories': categories})
