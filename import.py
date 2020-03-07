from api.models import Restaurant

import csv
res_arr = []
with open('japanese_cousine.csv') as csvfile:
    
    rows = csv.DictReader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        res_arr.append(Restaurant(**row))


Restaurant.objects.bulk_create(res_arr)