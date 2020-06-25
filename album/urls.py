from django.conf.urls import url
from . import views

urlpatterns = [
    
    url('^$',views.picture_of_day,name='albumToday')
]