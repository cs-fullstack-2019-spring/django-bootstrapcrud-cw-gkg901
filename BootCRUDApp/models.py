from django.db import models


# Create your models here.

class sellModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=9999999, decimal_places=2)
    pic = models.CharField(max_length=300, default='URL')

    def __str__(self):
        return self.name
