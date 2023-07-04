from django.shortcuts import render
from .forms import ProductForm

# creo la vista del formulario y le indico que hacer con los datos
def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form}) 
    else:
        form = ProductForm()
        return render(request, 'index.html', {'form': form})