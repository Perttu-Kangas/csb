from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import Account
from django.db.models import Q
import json


@login_required
def addView(request):
    user = request.user
    iban = request.POST.get("iban")

    Account.objects.create(owner=user, iban=iban)
    return redirect('/')


@login_required
def homePageView(request):
    user = request.user

    d = []

    accounts = Account.objects.filter(owner=user).values()
    for a in accounts:
        d.append(a)

    return render(request, 'pages/index.html', {'accounts': d})
