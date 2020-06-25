from django.db import models

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_lengh=20)
    second_name = models.CharField(max_lengh=20)
    email = models.EmailField()
