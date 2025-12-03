from django.urls import path, re_path

from Board import views

app_name = 'board'

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    re_path(r'<int:id>/detail')
]