from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def hem(request):
    innehall = {'poster' :Post.objects.all}
    return render(request, 'blogg/hem.html', innehall)

class PostLista(ListView):
    model=Post
    template_name='blogg/hem.html'
    context_object_name = 'poster'
    ordering = ['-datum_skapad']

class PostSida(DetailView):
    model=Post

class SkapaPost(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['titel', 'innehall']

    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)

class UppdaterPost(LoginRequiredMixin,UpdateView):
    model=Post
    fields = ['titel', 'innehall']

    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)

def om(request):
    return render(request, 'blogg/om.html',{'titel':'om'})

