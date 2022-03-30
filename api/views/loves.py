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
    
    def post(self, request):
        request.data['user'] = request.user.id
        love = LoveSerializer(data=request.data)
        if love.is_valid():
            love.save()
            return Response(love.data, status=status.HTTP_201_CREATED)
        else:
            return Response(love.errors, status=status.HTTP_400_BAD_REQUEST)

class LoveView(APIView):
    def get(self, request, pk):
        love = get_object_or_404(Love, pk=pk)
        # if request.user != love.user:
        #     raise PermissionDenied('Unauthorized, you are not signed in as this user')
        # else:
        data = LoveSerializer(love).data
        return Response(data)
    def delete(self, request, pk):
        love = get_object_or_404(Love, pk=pk)
        if request.user != love.user:
            raise PermissionDenied('Unauthorized, you are not signed in as this user')
        else:
            love.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
        love = get_object_or_404(Love, pk=pk)
        if request.user != love.owner:
            raise PermissionDenied('Unauthorized, you are not signed in as this user')
        else:
            updated_love = LoveSerializer(love, data=request.data)
        if updated_love.is_valid():
            updated_love.save()
            return Response(updated_love.data)
        else:
            return Response(love.errors, status=status.HTTP_400_BAD_REQUEST)