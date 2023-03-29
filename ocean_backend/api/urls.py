from django.urls import path

from api.controllers.data import get_data
from api.controllers.sort_controller import sort_api



urlpatterns = [
    
    path('sort', sort_api, name = 'sort'),
    path('data', get_data, name = 'data'),
    
    
    
]