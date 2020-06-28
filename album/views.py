from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Photos, Location


# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

def picture_of_day(request):
    date = dt.date.today()
    album = Photos.todays_album()
    locations = Location.objects.all()
    return render(request, 'all-photos/photos.html', {"date": date, "album": album, "locations": locations})
    
def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    album = Photos.objects.filter(location = selected_location.id)
    return render(request, 'all-photos/location.html', {"location":selected_location,"locations":locations,"album":album})    

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message": message})
        
def photos(request,photos_id):
    try:
        photos = Photos.objects.get(id = photos_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/photo.html", {"photos":photos})        

