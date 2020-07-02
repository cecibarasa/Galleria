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

class LocationTest(TestCase):
    def setUp(self):
        '''new instance before test'''
        self.nairobi = Location(name='nairobi')
        self.germany = Location(name='germany')

    def tearDown(self):
        Location.objects.all().delete()

    def test_location_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_location(self):
        self.nairobi.save_location()
        self.germany.save_location()
        location = Location.objects.all()
        self.assertEqual(len(location), 2)
        
    def test_delete_location(self):
        self.nairobi.save_location()
        location1= Location.objects.all()
        self.assertEqual(len(location1),1)
        self.nairobi.delete_location()
        location2= Location.objects.all()
        self.assertEqual(len(location2), 0)

    def test_update_location(self):
        self.nairobi.save_location()
        self.nairobi.update_location(self.nairobi.id,'maldives')
        update = Location.objects.get(name = "maldives")
        self.assertEqual(update.name, 'maldives')

    def test_display_locations(self):
        self.nairobi.save_location()
        self.germany.save_location()
        self.assertEqual(len(Location.display_all_locations()), 2)

class CategoryTest(TestCase):
    def setUp(self):
        
        self.nature = Category(name = "nature")
        self.entertainment = Category(name = "entertainment")

    def tearDown(self):
        
        Category.objects.all().delete()

    def test_category_instance(self):
        
        self.assertTrue(isinstance(self.nature, Category))
        self.assertTrue(isinstance(self.entertainment, Category))

    def test_save_category_method(self):
        self.nature.save_category()
        self.entertainment.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 2)

    def test_delete_category(self):
        
        self.nature.save_category()
        self.entertainment.save_category()
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),2)
        self.nature.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),1)

    def test_update_category(self):
        
        self.nature.save_category()
        self.nature.update_category(self.nature.id,'animals')
        update = Category.objects.get(name = "animals")
        self.assertEqual(update.name, 'animals')

class PhotosTestClass(TestCase):
    def setUp(self):
    
        self.nature = Category( name= "nature")
        self.nairobi = Location (name = "nairobi")
        self.art = Photos(photo_image = "art.jpg", name ='art', description = 'artistic', category= self.nature, location= self.nairobi)

    def tearDown(self):
       
        Photos.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_photo_instance(self):
       
        self.assertTrue(isinstance(self.art, Photos))

    def test_image_instance(self):
        
        self.assertTrue(isinstance(self.art, Photos))
          
    