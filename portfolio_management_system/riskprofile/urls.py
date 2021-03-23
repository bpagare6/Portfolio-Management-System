from django.urls import path
from . import views

urlpatterns = [
    path('risk-profile', views.risk_profile, name='risk-profile'),
]