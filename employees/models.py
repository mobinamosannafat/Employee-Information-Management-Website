from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    nationalCode =models.PositiveIntegerField()
    personalCode = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=200)
    #true means single false means married
    #maritialStatus = models.BooleanField()
    maritialStatus =models.CharField(max_length=7)
    age = models.PositiveSmallIntegerField()
    income =models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return '%s %s' % (self.name, self.family)
