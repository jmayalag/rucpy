from django.db import models

# Create your models here.
class Ruc(models.Model):
    ci = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=300)
    dv = models.IntegerField()