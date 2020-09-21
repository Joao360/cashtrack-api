from django.db import models

class MoneyDeposit(models.Model):
    owner = models.ForeignKey('users.User', related_name='money_deposit', on_delete=models.CASCADE)
    name = models.CharField("name of the deposit", max_length=64, blank=False, null=False)
    ammount = models.FloatField("ammount of cash present in the deposit", null=False, blank=False, default=0)

    class Meta:
        unique_together = ('owner', 'name')