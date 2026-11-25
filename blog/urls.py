from django.urls import path
from . import views

# Create your urls here

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('article/<int:id>', views.details, name = 'details')
]