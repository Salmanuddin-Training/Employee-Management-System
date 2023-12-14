from django.db import models
class Employees(models.Model):
    Eid = models.BigIntegerField()
    Ename = models.CharField(max_length = 255)
    Esal=models.IntegerField()
    Design=models.CharField(max_length = 255)
    Company=models.CharField(max_length = 255)
    Email=models.EmailField()
    Join_Date=models.DateField()
    City=models.DateField()


   
