from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()    

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
    photographer = models.ForeignKey(Photographer,on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(upload_to = 'photos/')


    def save_photo(self):
        self.save()

    def __str__(self):
        return self.name    

    @classmethod
    def search_by_category(cls,search_term):
        album = cls.objects.filter(category__name__icontains=search_term)
        return album

    @classmethod
    def todays_album(cls):
        # today = dt.date.today()
        album = cls.objects.filter()
        return album        