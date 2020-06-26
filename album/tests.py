from django.test import TestCase
from .models import Photographer, tag, Photos, Location, Category

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

# class PhotosTestCase(TestCase):
#     def setUp(self):
#         self.cecilia = Photos(name='Cecilia')
        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.cecilia, Photos))
            
#     def test_save_album(self):
#         self.cecilia.save_photo()
#         photos = Photos.objects.all()
#         assertTrue(len(photos) > 0)        