from django.views.generic import TemplateView
from django.shortcuts import render


class PaymentListView(TemplateView):
    template_name = 'payment/payment.html'


class InfoPayment(TemplateView):
    template_name = 'payment/info_payment.html'
