from django.db import models


class Salary(models.Model):
    account = models.IntegerField(null=False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)
    
    def __str__(self):
        return self.account


class Job(models.Model):
    title= models.CharField(max_length=15, blank=False, null=False)
    descrition = models.TextField(null=True)
    sarary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Coutry(models.Model):
    name=  models.CharField(max_length=15, blank=False, null=False)
    country_code =  models.CharField(max_length=6, blank=False, null=False)
    
    def __str__(self):
        return self.name  
    
    
class Location(models.Model):
    name =  models.CharField(max_length=30, blank=False, null=False)
    country = models.ForeignKey(Coutry, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name=  models.CharField(max_length=30, blank=False, null=False)
    address =  models.CharField(max_length=50, blank=False, null=False)
    rip_code =  models.CharField(max_length=5, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    


class Employee(models.Model):
    id_number= models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    


    

    
    
    
