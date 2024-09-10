from django.views.generic import FormView, TemplateView
from .forms import ForumMessages
from .models import ForumMessage
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ForumMessageView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')
    template_name = "forum/new_post.html"
    form_class = ForumMessages
    success_url = reverse_lazy('all')

    def form_valid(self, form):
        messages = form.save(commit=False)
        messages.sender = self.request.user
        messages.save()
        return super().form_valid(form)


class ForumView(TemplateView):
    template_name = 'forum/forum.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        context["messages"] = ForumMessage.objects.all()
        return super(ForumView, self).get_context_data(**context)
