from django.db import models
import uuid


# Create your models here.
STATUS =(('enable','Enable'),('disable','Disable'))
class Wallet(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owned_by= models.CharField(max_length=64, blank=True,null=True)
    status=models.CharField(max_length=64,choices=STATUS,null=True,blank=True)
    enabled_at=models.DateTimeField(null=True, blank=False)
    balance=models.IntegerField(null=True,blank=True)

    # def __str__(self):
    #     return self.id

class Deposite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=64,choices=STATUS, null=True, blank=True)
    deposited_at=models.DateTimeField(null=True, blank=False)
    enabled_at = models.DateTimeField(null=True, blank=False)
    amount=models.IntegerField(null=True,blank=True)
    reference_id=models.ForeignKey(Wallet,on_delete=models.SET_NULL, null=True,blank=True)

class Withdraw(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    withdrawn_by=models.ForeignKey(Wallet,on_delete=models.SET_NULL, null=True,blank=True)
    status=models.CharField(max_length=64,choices=STATUS, null=True, blank=True)
    amount=models.IntegerField(null=True,blank=True)
    reference_id=models.ForeignKey(Wallet,on_delete=models.SET_NULL, null=True,related_name="deposite_id")




