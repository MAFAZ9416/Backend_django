from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import 
from .models import articles

# Create your views here.

#login page
def login(request):
        

# Home page views
def home(request):
    
    # fetch the data from the database
    fetch_data = articles.objects.all()
    context = {
        'data' : fetch_data
    }

    return render(request, 'home.html', context)


# Details page views
def details(request, id):

    #Fetch the data from the database
    fetch_data = get_object_or_404(articles, id=id)
    context = {
        'data' : fetch_data
    }

    return render(request, 'details.html', context)


# Admin page views
def admin(request):
    
    return HttpResponse("Hi this is admin page")