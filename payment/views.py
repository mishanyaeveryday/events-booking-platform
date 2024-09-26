from django.shortcuts import render, get_object_or_404
from events.models import Categories, Events
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
# Create your views here.


def donate(request):
    categories = Categories.objects.all()
    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': 10,
        'item_name': 'DONATE',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('donate-success')}",
        'cancel_url': f"http://{host}{reverse('donate-failed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'events/donate.html', {'categories': categories, 'paypal': paypal_payment})


def DonateSuccess(request):
    categories = Categories.objects.all()
    return render(request, 'events/donate-success.html', {'categories': categories})


def DonateFailed(request):
    categories = Categories.objects.all()
    return render(request, 'events/donate-failed.html', {'categories': categories})
