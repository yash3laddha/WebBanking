from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, "home.html")

def custTable(request):
    customer = Customer.objects.all().order_by('Acc_No')
    return render(request, "custTable.html", {'customer': customer})

def trans(request, Acc):
    sender = Customer.objects.filter(Acc_No=Acc)
    context = {'sender':sender, 'Acc_No':Acc}
    return render( request, "trans.html", context)

def update_bal_req(request):
    Acc_Reciever = int(request.POST.get('reciever_acc_no'))
    Amt_Transfer = int(request.POST.get('amount_to_transfer'))
    reciever = Customer.objects.filter(Acc_No= Acc_Reciever)
    for a in reciever:
        rcb = a.Current_Balance
        
    Acc_Sender = int(request.POST.get('sender_acc_no'))
    sender = Customer.objects.filter(Acc_No = Acc_Sender)
    for b in sender:
        scb = b.Current_Balance
        
    amt_deb = scb - Amt_Transfer
    
    
    flag=0
    
    if Acc_Sender != Acc_Reciever:
        car=0
        if amt_deb < 0:
            flag=1
            sender = Customer.objects.filter(Acc_No = Acc_Sender)
            context={'car':car, 'flag':flag, 'sender': sender, 'Acc_No':Acc_Sender}
            return render(request, "trans.html", context)
        
        else:
            amt_cre = rcb + Amt_Transfer
            reciever = Customer.objects.filter(Acc_No= Acc_Reciever)
            for a in reciever:
                a.Current_Balance = amt_cre
                reciever_nam = a.Acc_Holder
                a.save()

            sender = Customer.objects.filter(Acc_No= Acc_Sender)
            for b in sender:
                b.Current_Balance = amt_deb
                sender_nam = b.Acc_Holder
                b.save()
            
            sender = Customer.objects.get(Acc_No = Acc_Sender)
            tsac=Transfer.objects.create(Acc_No = sender, amount_transferred=Amt_Transfer, acc_no_of_reciever=Acc_Reciever, updated_balance_of_reciever=amt_cre, updated_balance_of_sender=amt_deb, sender_name=sender_nam, reciever_name=reciever_nam)

            customer = Customer.objects.all().order_by('Acc_No')
            context = {'car':car, 'flag':flag, 'customer':customer}
            return render(request, "custTable.html", context)
    else:
        car=1
        sender = Customer.objects.filter(Acc_No = Acc_Sender)
        context={'car':car, 'sender': sender, 'Acc_No':Acc_Sender}
        return render(request, "trans.html", context)

def transfer_his(request):
    transfer = Transfer.objects.all().order_by('-id')
    return render(request, "transactionhistory.html", {'transfer': transfer})