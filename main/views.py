from django.shortcuts import render
from main.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserRead(APIView):
    def get(self, request, npm):
        try:
            user = User.objects.get(npm=npm)
            return Response({'status': 'OK', 'npm': user.npm, 'nama': user.nama}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'user tidak ditemukan'}, status=status.HTTP_404_NOT_FOUND)
