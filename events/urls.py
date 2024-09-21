from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.single_category, name='single_category'),

]
