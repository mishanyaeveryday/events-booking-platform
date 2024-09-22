from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from events.models import Categories, Events
from .serializer import CategoriesSeralizer, EventsSeralizer
# Create your views here.


@api_view(['GET'])
def get_categories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSeralizer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_events(request):
    events = Events.objects.all()
    serializer = EventsSeralizer(events, many=True)
    return Response(serializer.data)
