from rest_framework import serializers
from powerup.models.suprima import Suprima


class SuprimaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Suprima
        fields = ('name', 'location', 'unit')
        extra_kwargs = {
                        "name": {"error_messages": {"required": "provide the Name"}},
                        "location": {"error_messages": {"required": "provide the Location"}},
                        "unit": {"error_messages": {"required": "provide the UNIT"}},
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return Suprima.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.name = validated_data.get(
            "name", instance.name)
        instance.location = validated_data.get(
            "location", instance.location)
        instance.unit = validated_data.get(
            "unit", instance.unit)


class AllSuprimaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Suprima
        fields = ('uuid', 'name', 'tin', 'location', 'unit')
