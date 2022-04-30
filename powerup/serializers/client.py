from rest_framework import serializers
from powerup.models.client import Client


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('nid', 'firstname', 'lastname', 'phone', 'email', 'address', 'dob', 'gender',
                  'marital_status')
        extra_kwargs = {"nid": {"error_messages": {"required": "provide the National Id"}},
                        "firstname": {"error_messages": {"required": "provide the First Name"}},
                        "lastname": {"error_messages": {"required": "provide the Last Name"}},
                        "phone": {"error_messages": {"required": "provide the Phone Number"}},
                        "email": {"error_messages": {"required": "provide the Email"}},
                        "address": {"error_messages": {"required": "provide the Address"}},
                        "dob": {"error_messages": {"required": "provide the Date of Birth"}},
                        "gender": {"error_messages": {"required": "provide the Gender"}},
                        "marital_status": {"error_messages": {"required": "provide the Marital Status"}},
                        }

    def create(self, validated_data):
        """
        Create and return a new Attendance instance, given the validated data
        """
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Attendance instance, given the validated data
        """
        instance.nid = validated_data.get(
            "meeting_id", instance.meeting_id)
        instance.firstname = validated_data.get(
            "firstname", instance.firstname)
        instance.tel = validated_data.get(
            "lastname", instance.lastname)
        instance.phone = validated_data.get(
            "phone", instance.phone)
        instance.phone = validated_data.get(
            "email", instance.phone)
        instance.phone = validated_data.get(
            "address", instance.phone)
        instance.phone = validated_data.get(
            "dob", instance.phone)
        instance.phone = validated_data.get(
            "gender", instance.phone)
        instance.phone = validated_data.get(
            "marital_status", instance.phone)


class AllClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('uuid', 'firstname', 'lastname', 'phone', 'email', 'address', 'dob', 'gender',
                  'marital_status')
