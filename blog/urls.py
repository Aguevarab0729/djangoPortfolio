from django.urls import path
from .views  import render_about

urlpatterns = [
    path('', render_about, name='about'),
]
