from django.shortcuts import render, get_object_or_404
from .models import Categories, Events
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
# Create your views here.


def index(request):
    events = Events.objects.all()
    categories = Categories.objects.all()
    context = {
        'events': events,
        'categories': categories
    }
    return render(request, 'events/index.html', context)


def single_category(request, title):
    category = get_object_or_404(Categories, title=title)
    categories = Categories.objects.all()
    events = Events.objects.filter(category=category)
    return render(request, 'events/single_category.html', {'category': category, 'categories': categories, 'events': events})


def single_event(request, event_id):
    event = get_object_or_404(Events, event_id=event_id)
    categories = Categories.objects.all()
    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': event.price,
        'item_name': event.title,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'event_id': event_id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'event_id': event_id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'events/single_event.html', {'event': event, 'categories': categories, 'paypal': paypal_payment})


def PaymentSuccess(request, event_id):
    event = Events.objects.get(event_id=event_id)
    categories = Categories.objects.all()
    return render(request, 'events/payment-success.html', {'event': event, 'categories': categories})


def PaymentFailed(request, event_id):
    event = Events.objects.get(event_id=event_id)
    categories = Categories.objects.all()
    return render(request, 'events/payment-failed.html', {'event': event, 'categories': categories})
