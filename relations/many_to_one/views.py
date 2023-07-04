from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Articule
from datetime import date
# Create your views here.


def create(request):
    rep = Reporter(firs_name='ezequiel',last_name='Ezequiel', email= 'ezealeguzman@gmail.com')
    rep.save()
    

    art1= Articule(headline='El comienzo', pub_date=date(2023,6,26), reporter= rep)
    art1.save()
    art2= Articule(headline='El Medio', pub_date=date(2023,6,27), reporter= rep)
    art2.save()
    art3= Articule(headline='El Final', pub_date=date(2023,6,28), reporter= rep)
    art3.save()
    
    #acediendo del uno a muchos ponemos la clasecon el _set
    result = rep.articule_set.all()
  
    
    return HttpResponse(result)