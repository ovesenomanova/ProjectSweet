from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "info/main.html"


class ContactView(TemplateView):
    template_name = "info/contacts.html"


class OrderView(TemplateView):
    template_name = "info/order.html"