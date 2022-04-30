from rest_framework import serializers
from powerup.models.pivot import Pivot


class PivotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pivot
        fields = ('number', 'unit')
        extra_kwargs = {"number": {"error_messages": {"required": "provide the Pivot number"}},
                        "unit": {"error_messages": {"required": "provide the unit"}},
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return Pivot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.number = validated_data.get(
            "number", instance.number)
        instance.unit = validated_data.get(
            "unit", instance.unit)


class AllPivotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pivot
        fields = ('uuid', 'number', 'unit', 'longitude', 'latitude')
