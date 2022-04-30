from rest_framework import serializers
from powerup.models.account import Account
from powerup.serializers.client import AllClientSerializers
from powerup.serializers.suprima import AllSuprimaSerializers


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('phone', 'balance')
        extra_kwargs = {"phone": {"error_messages": {"required": "provide the phone number"}},
                        "balance": {"error_messages": {"required": "provide the balance"}},
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.phone = validated_data.get(
            "phone", instance.phone)
        instance.balance = validated_data.get(
            "balance", instance.balance)


class AllAccountSerializers(serializers.ModelSerializer):
    client = AllClientSerializers()
    suprima = AllSuprimaSerializers()

    class Meta:
        model = Account
        fields = ('uuid', 'phone', 'balance', 'created_at', 'client', 'suprima')
