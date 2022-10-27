from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import MyDetail
from .serializers import MyDetailSerializer

class ListMyDetail(generics.ListAPIView):
    queryset = MyDetail.objects.all()
    serializer_class = MyDetailSerializer


    