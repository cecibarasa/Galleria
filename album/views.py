from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def picture_of_day(request):
    
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def picture_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/photos.html', {"date": date,})

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

