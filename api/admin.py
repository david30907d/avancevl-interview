from django.contrib import admin
from api.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
admin.site.register(Restaurant, RestaurantAdmin)