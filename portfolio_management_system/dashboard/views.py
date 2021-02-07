import csv
import json
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Portfolio, StockHolding

# AlphaVantage API
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

def get_alphavantage_key():
  alphavantage_keys = [
    settings.ALPHAVANTAGE_KEY1,
    settings.ALPHAVANTAGE_KEY2,
    settings.ALPHAVANTAGE_KEY3,
    settings.ALPHAVANTAGE_KEY4,
    settings.ALPHAVANTAGE_KEY5,
    settings.ALPHAVANTAGE_KEY6,
    settings.ALPHAVANTAGE_KEY7,
  ]
  return random.choice(alphavantage_keys)

@login_required
def dashboard(request):
  portfolio = Portfolio.objects.get(user=request.user)
  portfolio.update_investment()
  holding_companies = StockHolding.objects.filter(portfolio=portfolio)
  holdings = []
  sectors = [[], []]
  sector_wise_investment = {}
  stocks = [[], []]
  for c in holding_companies:
    company_symbol = c.company_symbol
    company_name = c.company_name
    number_shares = c.number_of_shares
    investment_amount = c.investment_amount
    average_cost = investment_amount / number_shares
    holdings.append({
      'CompanySymbol': company_symbol,
      'CompanyName': company_name,
      'NumberShares': number_shares,
      'InvestmentAmount': investment_amount,
      'AverageCost': average_cost,
    })
    stocks[0].append(round((investment_amount / portfolio.total_investment) * 100, 2))
    stocks[1].append(company_symbol)
    if c.sector in sector_wise_investment:
      sector_wise_investment[c.sector] += investment_amount
    else:
      sector_wise_investment[c.sector] = investment_amount
  for sec in sector_wise_investment.keys():
    sectors[0].append(round((sector_wise_investment[sec] / portfolio.total_investment) * 100, 2))
    sectors[1].append(sec)
  context = {
    'holdings': holdings,
    'totalInvestment': portfolio.total_investment,
    'stocks': stocks,
    'sectors': sectors
  }

  return render(request, 'dashboard/dashboard.html', context)


def get_portfolio_insights(request):
  try:
    portfolio = Portfolio.objects.get(user=request.user)
    holding_companies = StockHolding.objects.filter(portfolio=portfolio)
    fd = FundamentalData(key=get_alphavantage_key(), output_format='json')
    portfolio_beta = 0
    portfolio_pe = 0
    for c in holding_companies:
      data, meta_data = fd.get_company_overview(symbol=c.company_symbol)
      portfolio_beta += float(data['Beta']) * (c.investment_amount / portfolio.total_investment)
      portfolio_pe += float(data['PERatio']) * (c.investment_amount / portfolio.total_investment)
    return JsonResponse({"PortfolioBeta": portfolio_beta, "PortfolioPE": portfolio_pe})
  except Exception as e:
    return JsonResponse({"Error": str(e)})


def update_values(request):
  try:
    portfolio = Portfolio.objects.get(user=request.user)
    current_value = 0
    unrealized_pnl = 0
    growth = 0
    holding_companies = StockHolding.objects.filter(portfolio=portfolio)
    stockdata = {}
    for c in holding_companies:
      ts = TimeSeries(key=get_alphavantage_key(), output_format='json')
      data, meta_data = ts.get_quote_endpoint(symbol=c.company_symbol)
      last_trading_price = float(data['05. price'])
      pnl = (last_trading_price * c.number_of_shares) - c.investment_amount
      net_change = pnl / c.investment_amount
      stockdata[c.company_symbol] = {
        'LastTradingPrice': last_trading_price,
        'PNL': pnl,
        'NetChange': net_change * 100
      }
      current_value += (last_trading_price * c.number_of_shares)
      unrealized_pnl += pnl
    growth = unrealized_pnl / portfolio.total_investment
    return JsonResponse({
      "StockData": stockdata, 
      "CurrentValue": current_value,
      "UnrealizedPNL": unrealized_pnl,
      "Growth": growth * 100
    })
  except Exception as e:
    return JsonResponse({"Error": str(e)})


def get_financials(request):
  try:
    fd = FundamentalData(key=get_alphavantage_key(), output_format='json')
    data, meta_data = fd.get_company_overview(symbol=request.GET.get('symbol'))
    financials = {
      "52WeekHigh": data['52WeekHigh'],
      "52WeekLow": data['52WeekLow'],
      "Beta": data['Beta'],
      "BookValue": data['BookValue'],
      "EBITDA": data['EBITDA'],
      "EVToEBITDA": data['EVToEBITDA'],
      "OperatingMarginTTM": data['OperatingMarginTTM'],
      "PERatio": data['PERatio'],
      "PriceToBookRatio": data['PriceToBookRatio'],
      "ProfitMargin": data['ProfitMargin'],
      "ReturnOnAssetsTTM": data['ReturnOnAssetsTTM'],
      "ReturnOnEquityTTM": data['ReturnOnEquityTTM'],
      "Sector": data['Sector'],
    }
    return JsonResponse({ "financials": financials })
  except Exception as e:
    return JsonResponse({"Error": str(e)})


def add_holding(request):
  if request.method == "POST":
    try:
      portfolio = Portfolio.objects.get(user=request.user)
      holding_companies = StockHolding.objects.filter(portfolio=portfolio)
      company_symbol = request.POST['company'].split('(')[1].split(')')[0]
      company_name = request.POST['company'].split('(')[0].strip()
      number_stocks = int(request.POST['number-stocks'])
      ts = TimeSeries(key=get_alphavantage_key(), output_format='json')
      data, meta_data = ts.get_daily(symbol=company_symbol, outputsize='full')
      buy_price = float(data[request.POST['date']]['4. close'])
      fd = FundamentalData(key=get_alphavantage_key(), output_format='json')
      data, meta_data = fd.get_company_overview(symbol=company_symbol)
      sector = data['Sector']

      found = False
      for c in holding_companies:
        if c.company_symbol == company_symbol:
          c.buying_value.append([buy_price, number_stocks])
          c.save()
          found = True

      if not found:
        c = StockHolding.objects.create(
          portfolio=portfolio, 
          company_name=company_name, 
          company_symbol=company_symbol,
          number_of_shares=number_stocks,
          sector=sector
        )
        c.buying_value.append([buy_price, number_stocks])
        c.save()

      return HttpResponse("Success")
    except Exception as e:
      print(e)
      return HttpResponse(e)

def send_company_list(request):
  with open('nasdaq-listed.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rows = []
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        rows.append([row[0], row[1]])
        line_count += 1
  return JsonResponse({"data": rows})