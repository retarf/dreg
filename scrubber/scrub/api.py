from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import WebsiteSerializer
from .models import WebsiteModel

class PullDataView(APIView):
    def post(self, request, format=None):
        serializer = WebSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebsiteView(viewsets.ModelViewSet):
    queryset = WebsiteModel.objects.all()
    serializer = WebsiteSerializer

