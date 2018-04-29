from django.db import models

# Create your models here.
class Pip(models.Model):
    title = models.CharField(max_length=90, unique=True)
    orgUnit = models.CharField(max_length=10)
    client = models.CharField(max_length=30)
    justification = models.TextField()
    objectives = models.TextField()
    cost_estimates = models.CharField(max_length=60)