from django.db import models
from .category import Category

RECORD_TYPES = (
    ("Income", "Income"),
    ("Expense", "Expense"),
)


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    money_deposit = models.ForeignKey(
        "records.MoneyDeposit", related_name="records", on_delete=models.CASCADE
    )
    recordType = models.CharField(choices=RECORD_TYPES, default="Income", max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField("amount of cash")
    entity = models.CharField(
        "the other entity in the tradeoff", max_length=64, blank=True
    )
    datetime = models.DateTimeField()
    note = models.CharField(max_length=256, blank=True)
