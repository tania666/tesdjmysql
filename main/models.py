#from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.

class Students(models.Model):
    sId=models.CharField(max_length=20)
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = "students"

class Suhu(models.Model):
    d_suhu = models.CharField(max_length=20)
    d_hum = models.CharField(max_length=20)

    class Meta:
        db_table = "suhu"