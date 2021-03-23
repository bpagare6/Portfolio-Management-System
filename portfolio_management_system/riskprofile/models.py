from django.db import models
from django.contrib.auth.models import User

class RiskProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  category = models.CharField(default='Conservative', max_length=30)
  age = models.CharField(default='under-30', max_length=30)
  emergency_funds = models.CharField(default='no-emergency-fund', max_length=30)
  investment_percentage = models.CharField(default='0-10-percent', max_length=30)
  high_reture_high_risk = models.CharField(default='disagree', max_length=30)
  expected_return_rate = models.CharField(default='12-percent', max_length=30)
  keep_capital_safe = models.CharField(default='agree', max_length=30)
  annual_take_home_income = models.CharField(default='2-5-lakh', max_length=30)
  worry_if_fall_percentage = models.CharField(default='less-5-percent', max_length=30)
  current_life_stage = models.CharField(default='single', max_length=30)
  investment_familiarity = models.CharField(default='somewhat-familiar', max_length=30)
  investment_length = models.CharField(default='3-5-years', max_length=30)
  work_status = models.CharField(default='is-secure', max_length=30)
  critical_situation_response = models.CharField(default='average-out', max_length=30)

  def __str__(self):
    return "User : " + str(self.user) + " -> Category : " + self.category