from django.test import TestCase
from .models import Photographer, tag, Photos, Location, Category
import datetime as dt

# Create your tests here.
class PhotographerTestCase(TestCase):
    def setUp(self):
        self.cecilia = Photographer(first_name='Cecilia', second_name='Barasa', email='ceciheroku@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.cecilia, Photographer))

    def test_save_method(self):
        self.cecilia.save_photographer()
        photogarphers = Photographer.objects.all()
        self.assertTrue(len(photogarphers) > 0)

class PhotosTestCase(TestCase):
    def setUp(self):
        self.cecilia = Photographer(first_name='cecilia', second_name='Barasa', email='ceciheroku@gmail.com')
        self.cecilia.save_photographer()
        
        self.new_tag = tag(name='cecilia')
        self.new_tag.save()

        self.new_location = Location(name='nairobi')
        self.new_location.save()

        self.new_category = Category(name='test')
        self.new_category.save()

        self.new_photos = Photos(name='Cecilia', description='Mama Rocks', photographer=self.cecilia)
        self.new_photos.save()

        self.new_photos.add(self.new_tag, self.new_category, self.new_location)

    def tearDown(self):
        Photographer.objects.all().delete()
        tag.objects.all().delete()
        Photos.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()                    