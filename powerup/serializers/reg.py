from rest_framework import serializers
from powerup.models.reg import REG


class REGSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = REG
        fields = ('client', 'location', 'pivot', 'phone')
        extra_kwargs = {"client": {"error_messages": {"required": "provide the Client Id"}},
                        "location": {"error_messages": {"required": "provide the Location"}},
                        "pivot": {"error_messages": {"required": "provide the Pivot number"}},
                        "phone": {"error_messages": {"required": "provide the Phone number"}}
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return REG.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.meeting_id = validated_data.get(
            "client", instance.meeting_id)
        instance.firstname = validated_data.get(
            "location", instance.firstname)
        instance.lastname = validated_data.get(
            "pivot", instance.lastname)
        instance.phone = validated_data.get(
            "phone", instance.phone)
