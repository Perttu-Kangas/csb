from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account


@login_required
def transferView(request):

    if request.method == 'POST':
        user = request.user
        to = User.objects.get(username=request.POST.get('to'))
        amount = int(request.POST.get('amount'))
        transfer(user, to, amount)

    return redirect('/')


@transaction.atomic
def transfer(sender, receiver, amount):
    if amount < 0 or sender == receiver:
        return

    acc1 = Account.objects.get(user=sender)

    if acc1.balance < amount:
        return

    acc2 = Account.objects.get(user=receiver)

    acc1.balance -= amount
    acc2.balance += amount

    acc1.save()
    acc2.save()


@login_required
def homePageView(request):
    accounts = Account.objects.exclude(user_id=request.user.id)
    return render(request, 'pages/index.html', {'accounts': accounts})
