from django.shortcuts import render
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ListNewsView(generics.ListAPIView):
	queryset = News.objects.all().order_by('-created_at')
	serializer_class = NewsSerializer
