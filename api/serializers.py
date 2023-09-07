from rest_framework import serializers
from .models import EndpointData

class EndpointDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndpointData
        fields = '__all__'