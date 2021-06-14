from django.db import models
from django.utils import timezone

class Customer(models.Model):
    Acc_No = models.IntegerField(primary_key = True)
    Acc_Holder = models.CharField(max_length = 200)
    Email_Id = models.EmailField(max_length = 200)
    Current_Balance = models.IntegerField()

    def __str__(self):
        return str(self.Acc_No)
    

class Transfer(models.Model):
    Acc_No = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount_transferred = models.IntegerField(default=0)
    acc_no_of_reciever = models.IntegerField(default=0)
    updated_balance_of_reciever= models.IntegerField(default=0)
    updated_balance_of_sender= models.IntegerField(default=0)
    sender_name=models.CharField(max_length=100)
    reciever_name=models.CharField(max_length=100)
    Date_Time=models.DateTimeField(default = timezone.now)

    #def __str__(self):
        #return self.Acc_No
        
