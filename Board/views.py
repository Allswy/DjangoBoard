from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Board
from .forms import BoardForm

# Create your views here.

class BoardListView(ListView):
    model = Board

    def get_queryset(self):
        return NotImplemented


class IndexView(ListView):
    model = Board
    template_name = 'board/index.html'
    context_object_name = 'boards_list'

    def get_queryset(self):
        return Board.objects.all()


class DetailView(DetailView):
    model = Board
    template_name = 'board/detail.html'


class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_form.html'
    success_url = reverse_lazy('board:index')
