# Create your views here.
from typing import Dict

from django.http import JsonResponse
from django.shortcuts import render
from api.models import Restaurant
from django.forms.models import model_to_dict

DAY_MAPPING = {
    "7": ('sun_start', 'sun_end'),
    "1": ('mon_start', 'mon_end'),
    "2": ('tue_start', 'tue_end'),
    "3": ('wed_start', 'wed_end'),
    "4": ('thur_start', 'thur_end'),
    "5": ('fri_start', 'fri_end'),
    "6": ('satur_start' 'satur_end')
}

def health_check(request) -> JsonResponse:
    return JsonResponse({"status": "success"}, safe=False)

def get_restaurant(request):
    day = request.GET.get('day')
    hour = request.GET.get('hour')
    minute = request.GET.get('minute')
    if hour and minute:
        print(day, hour, minute)
        restaurants = Restaurant.objects.all()
        restaurants_dict = [model_to_dict(r) for r in restaurants]
        return JsonResponse(restaurants_dict, safe=False)
    return JsonResponse([], safe=False)