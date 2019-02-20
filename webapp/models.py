from django.db import models

class Record(models.Model):
    ammount = models.FloatField("ammount of cash")
    description = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField("date of the record")
    subject = models.CharField(max_length=200)
