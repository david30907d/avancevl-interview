# -*- coding: utf-8 -*-
from django.conf.urls import url
from api import views

urlpatterns = [
  url(r'^get/restaurant$', views.get_restaurant, name='get_restaurant'),
]