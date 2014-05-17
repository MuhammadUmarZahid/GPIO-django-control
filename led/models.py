from django.db import models

# Create your models here.
class Led(models.Model):
    name=models.CharField(max_length=200)
    pin=models.IntegerField(default=0)
    stat=models.IntegerField(default=0)
    change=models.DateTimeField('date status changed')


