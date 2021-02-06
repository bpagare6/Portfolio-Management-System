from django.contrib import admin
from .models import Portfolio, StockHolding

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(StockHolding)