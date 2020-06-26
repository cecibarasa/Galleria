from django.conf.urls import url
from . import views

urlpatterns = [
    
    url('^$', views.picture_of_day, name='albumToday'),
    url(r'^search/', views.search_results, name='search_results')
]