from django.shortcuts import render, get_object_or_404
from .models import articles

# Create your views here.

# Home page views
def home(request):

    # fetch the data from the database
    fetch_data = articles.objects.all()
    context = {
        'data' : fetch_data
    }

    return render(request, 'home.html', context)


def details(request, id):

    #Fetch the data from the database
    fetch_data = get_object_or_404(articles, id=id)
    context = {
        'data' : fetch_data
    }

    return render(request, 'details.html', context)