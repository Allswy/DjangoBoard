from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('board/', include('Board.urls')),
    path('admin/', admin.site.urls),
]