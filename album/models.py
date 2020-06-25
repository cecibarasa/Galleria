from django.db import models

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class tag(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category        
