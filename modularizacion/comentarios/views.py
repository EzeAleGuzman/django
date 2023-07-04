from django.http import HttpResponse
from .models import Comentario

# Create your views here.
def test(request):
    return HttpResponse ('Esta es la pagina Test')

def create(request):
    #comentario = Comentario(name='Ezequiel',score='5', coment= 'Este es el comentario')
    #comentario.save()
    comentario = Comentario.objects.create(name='Micaela')
    return HttpResponse ('aqui se crea un dato')


def delete(request):
   # comentario = Comentario.objects.get(id=1)
   # comentario.delete()
   Comentario.objects.filter(id=2).delete()
   return HttpResponse('borradp de dato')