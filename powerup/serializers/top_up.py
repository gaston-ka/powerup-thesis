from rest_framework import serializers
from powerup.models.top_up import TopUp
from powerup.serializers.pivot import AllPivotSerializers
from powerup.serializers.account import AllAccountSerializers


class TopUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = TopUp
        fields = ('pivot_number', 'encr_message')
        extra_kwargs = {"new_unit": {"error_messages": {"required": "provide the new unit"}},
                        "encr_message": {"error_messages": {"required": "provide the message"}},
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return TopUp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.new_unit = validated_data.get(
            "new_unit", instance.new_unit)
        instance.unit = validated_data.get(
            "encr_message", instance.encr_message)


class AllTopUpSerializers(serializers.ModelSerializer):
    pivot_number = AllPivotSerializers()
    account = AllAccountSerializers()

    class Meta:
        model = TopUp
        fields = ('uuid', 'new_unit', 'balance', 'encr_message', 'top_up_date', 'pivot_number', 'account')
