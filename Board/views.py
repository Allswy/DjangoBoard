from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Board

# Create your views here.

class BoardListView(ListView):
    model = Board



class IndexView(ListView):
    model = Board
    template_name = ''