from django.db import models

RECORD_TYPES = ['Income', 'Expense']
CATEGORIES = ['FOOD', 'TECH', 'HOUSE', 'HEALTH', 'TAXES', 'TRANSPORTATION']

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Record(models.Model):
    recordType = models.CharField(choices=RECORD_TYPES, default='Income', max_length=64)
    #Add relation to category
    ammount = models.FloatField("ammount of cash")
    category = models.CharField(max_length=64)
    entity = models.CharField("the other entity in the tradeoff", max_length=64, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=256, blank=True)