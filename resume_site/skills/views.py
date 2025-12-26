from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def skills(request):
    return render(request, 'skills/skills.html')
