import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from powerup.models import Pivot
from powerup.models.reg import REG
from powerup.models.account import Account
from powerup.serializers.top_up import TopUpSerializers
from powerup.utility import get_encrypted_message
from powerup.models.top_up import TopUp


class TopUpView(APIView):
    def post(self, request):
        if "meter" in request.data and "phone" in request.data and "amount" in request.data:
            if REG.objects.filter(pivot__number=request.data["meter"]).exists():
                if Account.objects.filter(phone=request.data["phone"]).exists():
                    reg = REG.objects.get(pivot__number=request.data["meter"])
                    account = Account.objects.get(phone=request.data["phone"])
                    if account.balance >= float(request.data["amount"]):
                        topup_serializer = TopUpSerializers(data={
                            "encr_message": get_encrypted_message(),
                            "account": account,
                            "balance": float(request.data["amount"]),
                            "new_unit": float(request.data["amount"]) / 500,
                            "pivot_number": reg.pivot.id
                        })

                        if topup_serializer.is_valid(raise_exception=True):
                            topup = TopUp.objects.create(encr_message=get_encrypted_message(),
                                                         account=account,
                                                         balance=float(request.data["amount"]),
                                                         new_unit=float(request.data["amount"]) / 500,
                                                         pivot_number=reg.pivot)
                            account.balance = account.balance - float(request.data["amount"])
                            pivot = Pivot.objects.get(id=reg.pivot.id)
                            pivot.unit = pivot.unit + topup.new_unit
                            account.save()
                            pivot.save()

                            return Response(
                                {"Message": {"token": topup.encr_message,
                                             "Client": account.client.first_name + " " + account.client.last_name,
                                             "Balance": topup.balance,
                                             "Unit_purchased": topup.new_unit,
                                             "Total_Unit": pivot.unit,
                                             "completed_at": topup.top_up_date}},
                                status=status.HTTP_201_CREATED, )
                    else:
                        return Response(
                            {"Message": "Insufficient Amount"},
                            status=status.HTTP_201_CREATED, )
                else:
                    return Response(
                        {"Message": "Unknown phone number"},
                        status=status.HTTP_201_CREATED, )
            else:
                return Response(
                    {"Message": "Please provide valid pivot number"},
                    status=status.HTTP_201_CREATED, )
        else:
            return Response(
                {"Message": "Missing data"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        if "meter" in request.data:
            pass
        else:
            pass
