from django.urls import path
from django.conf.urls import url
from .views import ListNewsView
# from .views import CreateNewsView
from news import views

urlpatterns = [
    path('news/', ListNewsView.as_view(), name='news-api'),
    url(r'^news/create', views.create, name='created'),
]
