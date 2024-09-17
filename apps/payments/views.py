from django.views.generic import TemplateView
from .models import Payment


class PaymentListView(TemplateView):
    template_name = 'payment/payment.html'

