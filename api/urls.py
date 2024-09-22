from django.urls import path
from .views import get_categories, get_events

urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('events/', get_events, name='get_events'),
]
