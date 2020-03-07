# Create your views here.
from typing import Dict

from django.http import JsonResponse
from django.shortcuts import render
from api.models import Restaurant
from django.forms.models import model_to_dict

def health_check(request) -> JsonResponse:
    return JsonResponse({"status": "success"}, safe=False)

def get_restaurant(request):
    restaurants = Restaurant.objects.all()
    restaurants_dict = [model_to_dict(r) for r in restaurants]
    return JsonResponse(restaurants_dict, safe=False)