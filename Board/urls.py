from django.urls import path, re_path

from Board import views

app_name = 'board'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path('create/', views.BoardCreateView.as_view(), name='create'),
]