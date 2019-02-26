from django.db import models

class RecordType(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

class Record(models.Model):
    recordType = models.ForeignKey(RecordType, on_delete=models.CASCADE)
    ammount = models.FloatField("ammount of cash")
    category = models.CharField(max_length=64)
    entity = models.CharField("the other entity in the tradeoff", max_length=64, blank=True)
    datetime = models.DateTimeField("date of the record")
    note = models.CharField(max_length=256, blank=True)
