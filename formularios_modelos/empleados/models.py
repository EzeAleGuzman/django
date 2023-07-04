from django.db import models

# Create your models here.

class Empleados(models.Model):
    name = models.CharField(max_length=30,blank=False, null= False)
    last_name = models.CharField(max_length=30,blank=False, null= False)
    email = models.EmailField(max_length=50,blank=False, null=False)
    
    def __str__(self):
        return self.name