from django.db import models


class PurchasePlanningAnalysisData(models.Model):
    date_from = models.DateField(blank=False)
    date_to = models.DateField(blank=False)
    our_warehouse = models.CharField(max_length=200, blank=False)
    wb_warehouse = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    product = models.IntegerField(blank=True)
    cabinet = models.IntegerField(blank=True)
