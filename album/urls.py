from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    uurl('^today/$',views.picture_of_day,name='albumToday'))
]