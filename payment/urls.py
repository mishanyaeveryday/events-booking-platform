from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('donate-failed', views.DonateFailed, name='donate-failed'),
    path('donate-success', views.DonateSuccess, name='donate-success'),
]
