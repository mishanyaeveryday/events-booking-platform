from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:title>/', views.single_category, name='single_category'),
    path('payment-success/<uuid:event_id>/',
         views.PaymentSuccess, name='payment-success'),
    path('payment-failed/<uuid:event_id>/',
         views.PaymentFailed, name='payment-failed'),
    path('event/<uuid:event_id>/', views.single_event, name='single_event'),
]
