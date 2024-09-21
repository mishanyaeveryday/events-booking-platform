from django.shortcuts import render, get_object_or_404
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


def single_category(request, title):
    category = get_object_or_404(Categories, title=title)
    categories = Categories.objects.all()
    events = Events.objects.filter(category=category)
    return render(request, 'events/single_category.html', {'category': category, 'categories': categories, 'events': events})


def single_event(request, event_id):
    event = get_object_or_404(Events, event_id=event_id)
    categories = Categories.objects.all()
    return render(request, 'events/single_event.html', {'event': event, 'categories': categories})
