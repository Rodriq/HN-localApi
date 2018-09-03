from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

# from rest_framework.permissions import IsAuthenticated

# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# from rest_framework.parsers import JSONParser

# Create your views here.

class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer


# class CreateNewsView(generics.ListCreateAPIView):
#     # serializer = NewsSerializer(queryset, many=True)
#     serializer_class = NewsSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def create(request):
    data = JSONParser().parse(request)
    print(request.method)
    News.objects.create(title=data.get('title'), body=data.get('body'), url=data.get('url'))
    return JSONResponse(data)

# def trying(request, title, body):
# 	queryset = News.objects.get(title=title)
# 	return HttpResponse('{}'.format(body,title))
