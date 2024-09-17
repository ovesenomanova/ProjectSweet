from django.views.generic import View
from .models import Catalog, Basket
from django.shortcuts import redirect, reverse, render


class AddToBinView(View):
    def get(self, request, id):
        cake = Catalog.objects.filter(id=id)[0]
        return render( request, 'payment/payment.html', context={"cake": cake, } )
