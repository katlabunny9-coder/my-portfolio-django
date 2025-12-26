from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')

def resume_view(request):
    return render(request, "about/resume_viewer.html")

def about_page(request):
    return render(request, "about/about.html")
