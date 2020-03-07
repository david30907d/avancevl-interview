# Create your views here.
from typing import Dict

from django.http import JsonResponse
from django.shortcuts import render
from api.models import Restaurant
from django.forms.models import model_to_dict

DAY_MAPPING = {
    "1": '一',
    "2": '二',
    "3": '三',
    "4": '四',
    "5": '五',
    "6": '六',
    "7": '日'
}

def health_check(request) -> JsonResponse:
    return JsonResponse({"status": "success"}, safe=False)

from api.models import Restaurant

import csv
def get_restaurant(request):
    res_arr = []
    with open('japanese_cousine.csv') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            if '-' in row['日']      :
                sstart, send = row["日"].split('-')
                if ':' not in send :
                    send += ':00'
                if ':' not in sstart:
                    sstart += ':00'
            else:
                sstart = 'Closed'
                send = 'Closed'
            if '-' in row['一']  :
                mstart, mend = row["一"].split('-')
                if ':' not in mend :
                    mend += ':00'
                if ':' not in mstart:
                    mstart += ':00'
            else:
                mstart = 'Closed'
                mend = 'Closed'
            if '-' in row['二']  :
                tstart, tend = row["二"].split('-')
                if ':' not in tend :
                    tend += ':00'
                if ':' not in tstart:
                    tstart += ':00'
            else:
                tstart = 'Closed'
                tend = 'Closed'
            if '-' in row['三']  :
                wstart, wend = row["三"].split('-')
                if ':' not in wend :
                    wend += ':00'
                if ':' not in wstart:
                    wstart += ':00'
            else:
                wstart = 'Closed'
                wend = 'Closed'
            if '-' in row['四']  :
                tstart, tend = row["四"].split('-')
                if ':' not in tend :
                    tend += ':00'
                if ':' not in tstart:
                    tstart += ':00'
            else:
                tstart = 'Closed'
                tend = 'Closed'
            if '-' in row['五']  :
                fstart, fend = row["五"].split('-')
                if ':' not in fend :
                    fend += ':00'
                if ':' not in fstart:
                    fstart += ':00'
            else:
                fstart = 'Closed'
                fend = 'Closed'
            if '-' in row['六']  :
                ssstart, ssend = row["六"].split('-')
                if ':' not in ssend :
                    ssend += ':00'
                if ':' not in ssstart:
                    ssstart += ':00'
            else:
                ssstart = 'Closed'
                ssend = 'Closed'
            row['sun_start'] = sstart
            row['mon_start'] = mstart
            row['tue_start'] = tstart
            row['wed_start'] = wstart
            row['thur_start'] = tstart
            row['fri_start'] = fstart
            row['satur_start'] = ssstart
            row['sun_end'] = send
            row['mon_end'] = mend
            row['tue_end'] = tend
            row['wed_end'] = wend
            row['thur_end'] = tend
            row['fri_end'] = fend
            row['satur_send'] = ssend
            row = dict(row)
            del row['日']
            del row['一']
            del row['二']
            del row['三']
            del row['四']
            del row['五']
            del row['六']
            res_arr.append(Restaurant(**row))


    Restaurant.objects.bulk_create(res_arr)


    day = request.GET.get('day')
    hour = request.GET.get('hour')
    minute = request.GET.get('minute')
    if hour and minute:
        print(day, hour, minute)
        restaurants = Restaurant.objects.filter()
        restaurants_dict = [model_to_dict(r) for r in restaurants]
        return JsonResponse(restaurants_dict, safe=False)
    return JsonResponse([], safe=False)