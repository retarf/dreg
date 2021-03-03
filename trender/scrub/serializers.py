from rest_framework import serializers

from .models import WebsiteModel

class WebsiteSerializer(serializers.Serializer):
    class Meta:
        model = WebsiteModel
        fields = ['__all__']
