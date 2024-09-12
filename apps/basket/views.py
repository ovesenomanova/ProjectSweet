from django.views import View
from .models import Catalog, Basket
from django.shortcuts import redirect, reverse


class AddToBinView(View):
    def post(self, request, id):
        user = request.user
        cake = Catalog.objects.filter(id=id)[0]
        new_bin = Basket(user=user, cake=cake)
        new_bin.save()
        return redirect( reverse('catalog') )


