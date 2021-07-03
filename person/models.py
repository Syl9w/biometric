from django.db import models

# Create your models here.

class Person(models.Model):
    iin = models.CharField(max_length=12)
    years = models.IntegerField()
    def __str__(self):
        return "-".join(self.iin[:2],self.iin[2:4], self.iin[4:6])