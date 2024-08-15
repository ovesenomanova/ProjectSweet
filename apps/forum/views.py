from django.http import HttpRequest
from . import forms
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ForumMessages
from django.urls import reverse_lazy


def forum(request: HttpRequest):
    template_kwards = {
        'user': request.user
    }
    return render(request, 'forum/titul.html', template_kwards)


class ForumMessageView(FormView):
    template_name = "forum/new_post.html"
    form_class = ForumMessages
    success_url = reverse_lazy('all')


def new_post(request: HttpRequest):
    if request.method == 'GET':
        template_kwargs = {
            'form': forms.ForumMessages()
        }
        return render(request, 'forum/new_post.html', template_kwargs)
    #добавление нового сообщения сделать тут
    return redirect( forum )

def all(request: HttpRequest):
    template_kwards = {
        'user': request.user
    }
    return render(request, 'forum/all.html', template_kwards)