from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.get_categories, name='get_categories'),
    path('events/', views.get_events, name='get_events'),
    path('categories/<str:title>/', views.category_detail, name='category_detail'),
    path('events/<uuid:event_id>/', views.event_detail, name='event_detail'),
]
