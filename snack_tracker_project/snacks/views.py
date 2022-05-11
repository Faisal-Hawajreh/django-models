from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Snack

# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks_list'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack