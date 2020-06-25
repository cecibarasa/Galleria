from django.db import models

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)