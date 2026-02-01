from rest_framework import serializers
from .models import WorkshopRegistration

class WorkshopRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopRegistration
        fields = "__all__"