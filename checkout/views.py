from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QhrWHGLG50LDIYR35Z8xzuA6aCINdqsFqB5C4lN6y2gHNxu9xJgRh8xcfDDge2DEE7zvd3CR63TCDxZUNnUG7lN00uqpmkneT',
        'client_secret': 'test client_secret',
    }

    return render(request, template, context)