from django.views.generic import TemplateView
from .models import Catalog

class CatalogView(TemplateView):
    template_name = 'cakes/child.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)

        context['items'] = ['img/child_1.jpeg', 'img/child_2.jpeg', 'img/child_3.jpeg', 'img/child_4.jpeg']
        return context


class CakesListView(TemplateView):
    template_name = 'cakes/cakelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cakes"] = Catalog.objects.all()
        return context

