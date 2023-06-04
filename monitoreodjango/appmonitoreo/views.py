from django.shortcuts import render
from .models import Paciente_clin


# Create your views here.

def home(request):
    paciente=Paciente_clin.objects.all()
    data={
        'paciente': paciente
    }
    return render(request, 'appmonitoreo/home.html', data)


      