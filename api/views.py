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


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, title):
    try:
        category = Categories.objects.get(title=title)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriesSeralizer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriesSeralizer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, event_id):
    try:
        event = Events.objects.get(event_id=event_id)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventsSeralizer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventsSeralizer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
