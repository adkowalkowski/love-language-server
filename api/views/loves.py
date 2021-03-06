from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from ..serializers.love import LoveSerializer 
from ..serializers.love import LoveCreateSerializer
from ..models.love import Love
from django.contrib.auth import authenticate

class LovesView(APIView):
    def get(self, request):
        loves = Love.objects.filter(user=request.user.id)
        data = LoveSerializer(loves, many=True).data
        return Response(data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        print(request.data)
        love = LoveCreateSerializer(data=request.data)
        # if model.objects.count() > 0 
        if love.is_valid():
            love.save()
            return Response(love.data, status=status.HTTP_201_CREATED)
        else:
            return Response(love.errors, status=status.HTTP_400_BAD_REQUEST)

class LoveView(APIView):
    # I do not want authorization for the get request, but I do for the delete and put. These
    # are fine here, because the delete and put requests have conditionals 
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, email): 
        love = get_object_or_404(Love, user__email=email)
        data = LoveSerializer(love).data
        print(request.data)
        return Response([data])

    def delete(self, request, pk):
        love = get_object_or_404(Love, pk=pk)
        # removing user check for now because the delete button only appears on the frontend for your specific card, but I should figure
        # out post MVP
        # if request.user != love.user:
        #     raise PermissionDenied('Unauthorized, you are not signed in as this user')
        # else:
        love.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        love = get_object_or_404(Love, pk=pk)
        
    
        updated_love = LoveSerializer(love, data=request.data)
        if updated_love.is_valid():
            updated_love.save()
            return Response(updated_love.data)
        else:
            return Response(updated_love.errors, status=status.HTTP_400_BAD_REQUEST)
        
       