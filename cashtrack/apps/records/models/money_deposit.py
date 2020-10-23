from django.db import models


class MoneyDeposit(models.Model):
    owner = models.ForeignKey(
        "users.User", related_name="money_deposits", on_delete=models.CASCADE
    )
    name = models.CharField(
        "name of the deposit", max_length=64, blank=False, null=False
    )
    initial_amount = models.FloatField(
        "amount of cash present in the deposit when it was registered",
        null=False,
        blank=False,
        default=0,
    )

    class Meta:
        unique_together = ("owner", "name")
