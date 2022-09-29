from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .models import Location

# from django.template import loader

def show_all_locations(request):
    locations = Location.objects.all()
    context = {'displayLocations' : locations, 'pageTitle': 'Tourism'}
    return render(request, 'location/index.html', context)  

def show_category_locations(request, categoryname):
    try:
        locations = Location.objects.filter(categoryid__name__iexact = categoryname)
        # print(locations.query)
        # for location in locations:
            # print(location)
        if locations.count() > 0:
            # return HttpResponse(f'<h1>Display all of the locations of type {categoryname}</h1>')
            context = {'displayLocations' : locations, 'categoryName' : categoryname}
            return render(request, 'location/index.html', context)  
        else:
            return HttpResponse(f'<h1>Unable to locate any items in our database of type {categoryname}</h1>')
    except: 
        return HttpResponse(f'<h1>Unable to locate any locations of type {categoryname}</h1>')

