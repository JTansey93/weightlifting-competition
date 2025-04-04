from django.db import models

# Create your models here.
class Competitor(models.Model):
    name = models.CharField(max_length=32)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    bodyweight = models.DecimalField(max_digits=5, decimal_places=2)
    snatchFirstAttempt = models.IntegerField()
    cnjFirstAttempt = models.IntegerField()
    