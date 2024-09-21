from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:title>/', views.single_category, name='single_category'),
    path('event/<uuid:event_id>/', views.single_event, name='single_event'),
]
