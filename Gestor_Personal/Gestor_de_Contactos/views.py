from django.shortcuts import render,get_object_or_404, redirect
from .forms import ContactoForm
from .models import Contacto



def index(request):
    contactos = Contacto.objects.all()
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Contacto.objects.filter(email=email).exists():
                form.add_error('email', 'Este email ya esta siendo usado')
            else:
                form.save()
    else:
        form = ContactoForm()
        
    return render(request, 'index.html', {'form': form, 'contactos': contactos})
    
def borrar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    contacto.delete()
    return redirect('index')

def editar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Contacto.objects.filter(email=email).exclude(id=contacto_id).exists():
                form.add_error('email', 'Este email ya está siendo usado')
            else:
                form.save()
                return redirect('index')
    else:
        form = ContactoForm(instance=contacto)
    
    return render(request, 'editar_contacto.html', {'form': form, 'contacto_id': contacto_id})