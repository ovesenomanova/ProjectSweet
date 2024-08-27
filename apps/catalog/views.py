from django.views.generic import TemplateView
from .models import Catalog


class CakesListView(TemplateView):
    template_name = 'cakes/child.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Catalog.objects.all()
        return context
