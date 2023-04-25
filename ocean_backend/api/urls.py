from django.urls import path

from api.controllers.data import get_data
from api.controllers.sort_controller import sort_api
from api.controllers.table_calculations import table_calc_api



urlpatterns = [
    
    path('sort', sort_api, name = 'sort'),
    path('data', get_data, name = 'data'),
    path('table', table_calc_api, name = 'data'),
    
    
    
    
]