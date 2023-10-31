from django.db import models


class PurchasePlanningAnalysisData(models.Model):
    date_from = models.DateField(null=False)
    date_to = models.DateField(null=False)
    our_warehouse = models.CharField(max_length=200, null=False)
    wb_warehouse = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    product = models.IntegerField(null=True)
    cabinet = models.IntegerField(null=True)
