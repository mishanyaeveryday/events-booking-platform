from django.shortcuts import render, get_object_or_404
from events.models import Categories, Events
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
# Create your views here.


def donate(request):
    categories = Categories.objects.all()
    return render(request, 'events/donate.html', {'categories': categories})


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
    return render(request, 'payment-success.html', {'event': event, 'categories': categories})


def PaymentFailed(request, event_id):
    event = Events.objects.get(event_id=event_id)
    categories = Categories.objects.all()
    return render(request, 'payment-failed.html', {'event': event, 'categories': categories})
