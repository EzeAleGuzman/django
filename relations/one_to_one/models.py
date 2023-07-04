from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    
    
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete= models.CASCADE, primary_key= True)
    Number_of_employess = models.IntegerField(default=1)
    
    def __str__(self):
        return self.place.name