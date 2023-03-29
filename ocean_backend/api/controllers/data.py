from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
import json

from api.cache.cache_data import set_cache_data


@api_view(['POST'])  
def get_data(request):
    if request.method == 'POST':
        
        # import the data from the frontend in bytes format 
        file_data_bytes = request.body.decode()
        
        # convert the data into a json format as python dictionary type
        data_dict = json.loads(file_data_bytes)
        
        # saving the data into cache for business logic purpose
        set_cache_data(data_dict)
    
    return HttpResponse('ok', status = 200)