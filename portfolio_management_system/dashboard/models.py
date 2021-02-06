from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class Portfolio(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  total_investment = models.FloatField(default=0)

  def update_investment(self):
    investment = 0
    holdings = StockHolding.objects.filter(portfolio=self)
    for c in holdings:
      investment += c.investment_amount
    self.total_investment = investment
    self.save()

  def __str__(self):
    return "Portfolio : " + str(self.user)


class StockHolding(models.Model):
  portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
  company_symbol = models.CharField(default='', max_length=25)
  company_name = models.CharField(max_length=100)
  sector = models.CharField(default='', max_length=50)
  number_of_shares = models.IntegerField(default=0)
  investment_amount = models.FloatField(default=0)
  buying_value = JSONField(default=list)

  def save(self, *args, **kwargs):
    inv_amount = 0.0
    num_shares = 0
    for price, quantity in self.buying_value:
      inv_amount += price * quantity
      num_shares += quantity
    self.investment_amount = inv_amount
    self.number_of_shares = num_shares
    super(StockHolding, self).save(*args, **kwargs)

  def __str__(self):
    return str(self.portfolio) + " -> " + self.company_symbol + " " + str(self.number_of_shares)