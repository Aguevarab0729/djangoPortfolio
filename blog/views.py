from django.shortcuts import render
from .models import About

def render_about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})