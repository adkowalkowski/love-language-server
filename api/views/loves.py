from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from ..serializers.love import LoveSerializer 
from ..models.love import Love

class LovesView(APIView):
    def get(self, request):
        loves = Love.objects.filter(user=request.user.id)
        data = LoveSerializer(loves, many=True).data
        return Response(data)