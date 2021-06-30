from rest_framework import serializers
from .models import *

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields="__all__"


class DepositeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deposite
        fields="__all__"

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model=Withdraw
        fields= "__all__"
