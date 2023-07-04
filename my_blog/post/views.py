from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

#aCTUALIZAR DATOS
def update(request):
    author = Author.objects.get(id = 1)
    author.name= 'Ezequiel'
    author.email= 'ezealeguzman@gmail.com'
    author.save()
    return HttpResponse('Dato actualizado')

# consultar datos
def queries(request):
    #obtener todos los elementos
    authors = Author.objects.all()
    
    #obtener datos filtrados por condicion
    filtered = Author.objects.filter(email='brian63@example.com')
    
    #obtener objeto unico
    author  = Author.objects.get(id = 1)
    
    ##obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]
    
    #obtener 5 elementos saltado los 5 primeros
    offsets = limits = Author.objects.all()[5:10]
    
     #obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')
    
    #obtener todos los elemntos id <= 15(__lte: menor o igual, lt: mayor que....buscarlas demas codigos de operadores)
    filtereds =  filtered = Author.objects.filter(id__lte=15)
    
    #obtener todos los autores que contienen en su nombre la palabra yes
    contains =  filtered = Author.objects.filter(name__contains='yes')
    
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtereds': filtereds, 'contains': contains })
    

