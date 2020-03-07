from django.db import models


class Restaurant(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    日 = models.CharField(max_length=40)
    一 = models.CharField(max_length=40)
    二 = models.CharField(max_length=40)
    三 = models.CharField(max_length=40)
    四 = models.CharField(max_length=40)
    五 = models.CharField(max_length=40)
    六 = models.CharField(max_length=40)
    類型 = models.CharField(max_length=40)
    米其林星 = models.CharField(max_length=40)
    停車 = models.CharField(max_length=40)
    外送 = models.CharField(max_length=40)
    先繳訂金 = models.CharField(max_length=40)
    評價 = models.FloatField(max_length=40)
    地理位子 = models.CharField(max_length=40)