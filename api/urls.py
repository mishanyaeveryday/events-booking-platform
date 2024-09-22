from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('categories/', views.get_categories, name='get_categories'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<str:title>/', views.category_detail, name='category_detail'),
    path('categories/<str:title>/info/',
         views.get_category, name='get_category'),

    path('events/', views.get_events, name='get_events'),
    path('events/<uuid:event_id>/', views.event_detail, name='event_detail'),
    path('events/<uuid:event_id>/info/', views.get_event, name='get_event'),
    path('events/create/', views.event_create, name='event_create'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
