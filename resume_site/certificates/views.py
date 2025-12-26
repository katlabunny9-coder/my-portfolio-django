from django.shortcuts import render

# Create your views here.
def certificates(request):
    return render(request, 'certificates/certificates.html')
from django.shortcuts import render
from .models import Certificate

def certificates(request):
    certs = Certificate.objects.all()
    return render(request, 'certificates/certificates.html', {'certs': certs})
