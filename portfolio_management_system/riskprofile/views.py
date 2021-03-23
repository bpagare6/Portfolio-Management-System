from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import RiskProfile

@login_required
def risk_profile(request):
  if request.method == "GET":
    return render(request, 'riskprofile/risk-profile.html')
  elif request.method == "POST":
    q1_option = request.POST['q1-option']
    q2_option = request.POST['q2-option']
    q3_option = request.POST['q3-option']
    q4_option = request.POST['q4-option']
    q5_option = request.POST['q5-option']
    q6_option = request.POST['q6-option']
    q7_option = request.POST['q7-option']
    q8_option = request.POST['q8-option']
    q9_option = request.POST['q9-option']
    q10_option = request.POST['q10-option']
    q11_option = request.POST['q11-option']
    q12_option = request.POST['q12-option']
    q13_option = request.POST['q13-option']

    print(q1_option, q2_option, q3_option, q4_option, q5_option, q6_option, q7_option, q8_option, q9_option, q10_option, q11_option, q12_option, q13_option)

    # Question 1
    if q1_option == 'under-30':
      q1_option_val = 5
    elif q1_option == '30-40':
      q1_option_val = 4
    elif q1_option == '40-50':
      q1_option_val = 3
    elif q1_option == '50-60':
      q1_option_val = 2
    else:
      q1_option_val = 1

    # Question 2
    if q2_option == 'no-emergency-fund':
      q2_option_val = 1
    elif q2_option == 'less-3-months':
      q2_option_val = 2
    elif q2_option == '4-6-months':
      q2_option_val = 3
    elif q2_option == '7-9-months':
      q2_option_val = 4
    else:
      q2_option_val = 5

    # Question 3
    if q3_option == '0-10-percent':
      q3_option_val = 2
    elif q3_option == '11-20-percent':
      q3_option_val = 3
    elif q3_option == '21-30-percent':
      q3_option_val = 4
    elif q3_option == 'more-30-percent':
      q3_option_val = 5 
    else:
      q3_option_val = 1

    # Question 4
    if q4_option == 'strongly-agree':
      q4_option_val = 5
    elif q4_option == 'agree':
      q4_option_val = 4
    elif q4_option == 'neutral':
      q4_option_val = 3
    elif q4_option == 'disagree':
      q4_option_val = 2
    else:
      q4_option_val = 1

    # Question 5
    if q5_option == '6-percent':
      q5_option_val = 1
    elif q5_option == '10-percent':
      q5_option_val = 2
    elif q5_option == '12-percent':
      q5_option_val = 3
    elif q5_option == '15-percent':
      q5_option_val = 4
    else:
      q5_option_val = 5

    # Question 6
    if q6_option == 'strongly-agree':
      q6_option_val = 1
    elif q6_option == 'agree':
      q6_option_val = 2
    elif q6_option == 'neutral':
      q6_option_val = 3
    elif q6_option == 'disagree':
      q6_option_val = 4
    else:
      q6_option_val = 5

    # Question 7
    if q7_option == 'under-2-lakh':
      q7_option_val = 1
    elif q7_option == '2-5-lakh':
      q7_option_val = 2
    elif q7_option == '5-10-lakh':
      q7_option_val = 3
    elif q7_option == '10-20-lakh':
      q7_option_val = 4
    else:
      q7_option_val = 5

    # Question 8
    if q8_option == 'less-5-percent':
      q8_option_val = 1
    elif q8_option == '5-10-percent':
      q8_option_val = 2
    elif q8_option == '10-20-percent':
      q8_option_val = 3
    elif q8_option == '20-30-percent':
      q8_option_val = 4
    else:
      q8_option_val = 5

    # Question 9
    if q9_option == 'single':
      q9_option_val = 5
    elif q9_option == 'couple-without-child':
      q9_option_val = 4
    elif q9_option == 'young-family':
      q9_option_val = 3
    elif q9_option == 'mature-family':
      q9_option_val = 5
    elif q9_option == 'preparing-retirement':
      q9_option_val = 2
    else:
      q9_option_val = 1

    # Question 10
    if q10_option == 'not-familiar-uncomfortable':
      q10_option_val = 0
    elif q10_option == 'not-familiar':
      q10_option_val = 1
    elif q10_option == 'somewhat-familiar':
      q10_option_val = 2
    elif q10_option == 'fairly-familiar':
      q10_option_val = 3
    else:
      q10_option_val = 5

    # Question 11
    if q11_option == '2-years-or-less':
      q11_option_val = 1
    elif q11_option == '3-5-years':
      q11_option_val = 3
    elif q11_option == '6-10-years':
      q11_option_val = 4
    else:
      q11_option_val = 5

    # Question 12
    if q12_option == 'is-not-dependable':
      q12_option_val = 2
    elif q12_option == 'is-secure':
      q12_option_val = 5
    elif q12_option == 'enough-wealth':
      q12_option_val = 4
    else:
      q12_option_val = 3

    # Question 13
    if q13_option == 'average-out':
      q13_option_val = 5
    elif q13_option == 'do-not-bother':
      q13_option_val = 4
    elif q13_option == 'book-loss':
      q13_option_val = 1
    else:
      q13_option_val = 2

    total_score = q1_option_val + q2_option_val + q3_option_val + \
                  q4_option_val + q5_option_val + q6_option_val + \
                  q7_option_val + q8_option_val + q9_option_val + \
                  q10_option_val + q11_option_val + q12_option_val + q13_option_val

    category = ''
    if total_score <= 24:
      category = 'Conservative'
    elif total_score <= 40:
      category = 'Balanced'
    elif total_score <= 52:
      category = 'Assertive'
    else:
      category = 'Aggressive'

    try:
      RiskProfile.objects.create(user=request.user, age=q1_option, emergency_funds=q2_option,
                                 investment_percentage=q3_option, high_reture_high_risk=q4_option,
                                 expected_return_rate=q5_option, keep_capital_safe=q6_option,
                                 annual_take_home_income=q7_option, worry_if_fall_percentage=q8_option,
                                 current_life_stage=q9_option, investment_familiarity=q10_option,
                                 investment_length=q11_option, work_status=q12_option,
                                 critical_situation_response=q13_option, category=category)
    except Exception as e:
      return HttpResponse('Error : ' + str(e))

    return redirect('dashboard')