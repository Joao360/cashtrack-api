from django.db import models

RECORD_TYPES = (
    ('Income', 'Income'),
    ('Expense', 'Expense'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Record(models.Model):
    recordType = models.CharField(choices=RECORD_TYPES, default='Income', max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ammount = models.FloatField("ammount of cash")
    entity = models.CharField("the other entity in the tradeoff", max_length=64, blank=True)
    datetime = models.DateTimeField()
    note = models.CharField(max_length=256, blank=True)