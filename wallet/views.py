from django.shortcuts import render
from .models import *
from .serializers import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .permissions import IsGETOrPatch


# Create your views here.

class WalletAPIView(APIView):
    def get(self,request,format=None):
        survey=Wallet.objects.all()
        serializer=WalletSerializer(survey,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=DepositeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_active = False
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DepositeAPIView(APIView):
    def get(self,request,format=None):
        survey=Deposite.objects.all()
        serializer=DepositeSerializer(survey,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=DepositeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_active = False
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WithdrawAPIView(APIView):
    def get(self,request,format=None):
        survey=Withdraw.objects.all()
        serializer=WithdrawSerializer(survey,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=WithdrawSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_active = False
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class WalletCbv(ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer
    authentication_classes=[TokenAuthentication,]
    pemission_classes=[IsGETOrPatch,]


