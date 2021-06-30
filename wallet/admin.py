from django.contrib import admin
from .models import *
# Register your models here.

class WalletAdmin(admin.ModelAdmin):
    list_display = ['id','owned_by','status','enabled_at','balance']


class DepositeAdmin(admin.ModelAdmin):
    list_display = ['id','status','deposited_at','enabled_at','amount','reference_id']

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['id','withdrawn_by','status','amount','reference_id']


admin.site.register(Wallet,WalletAdmin)
admin.site.register(Deposite,DepositeAdmin)
admin.site.register(Withdraw,WithdrawAdmin)
