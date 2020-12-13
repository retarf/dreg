from rest_framework import serializers

class WebSerializer(serializers.Serializer):
    url = serializers.URLField(allow_blank=False)
    name = serializers.CharField(allow_blank=False)
