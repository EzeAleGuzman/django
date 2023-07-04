from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def create(request):
    
    place = Place(name='Santa Catalina', address='Calle falsa 123')
    place.save()
    
    restaurant = Restaurant(place=place,Number_of_employess=8)
    restaurant.save()
    
    
    return HttpResponse(restaurant.place.name)

