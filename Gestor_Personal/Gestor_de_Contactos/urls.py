from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('borrar/<int:contacto_id>/', views.borrar_contacto, name='borrar_contacto'),
    path('editar/<int:contacto_id>/', views.editar_contacto, name='editar_contacto'),
]
