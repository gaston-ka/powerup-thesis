from rest_framework import serializers
from powerup.models.emergency import Emergency
from powerup.serializers.pivot import AllPivotSerializers


class EmergencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ('pivot_number', 'message')
        extra_kwargs = {"pivot_number": {"error_messages": {"required": "provide the Pivot number"}},
                        "message": {"error_messages": {"required": "provide the message"}},
                    }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return Emergency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.pivot_number = validated_data.get(
            "pivot_number", instance.pivot_number)
        instance.unit = validated_data.get(
            "message", instance.message)


class AllEmergencySerializers(serializers.ModelSerializer):
    pivot_number = AllPivotSerializers()

    class Meta:
        model = Emergency
        fields = ('uuid', 'pivot_number', 'message', 'reg_tel')
