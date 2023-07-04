from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadosForm

# Create your views here.

def index(request):
    form = EmpleadosForm
    return render(request, 'index.html', {'form': form})