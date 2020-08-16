from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from rest_framework import status as http_status
from django.core import serializers
from .serializers import UserSerializer
import traceback

# Create your views here.
@api_view(['GET'])
def get_user_data(request):
    try:
        serialzer = UserSerializer(User.objects.all(), many=True)
        return Response({"ok": True, "members": serialzer.data}, 
        content_type='application/json', 
        status=http_status.HTTP_200_OK)
    except:
        traceback.print_exc()
        Response({"ok": False, "members": []}, 
        content_type='application/json', 
        status=http_status.HTTP_400_BAD_REQUEST)
    