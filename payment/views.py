from django.shortcuts import render
from events.models import Categories
# Create your views here.


def donate(request):
    categories = Categories.objects.all()
    return render(request, 'events/donate.html', {'categories': categories})
