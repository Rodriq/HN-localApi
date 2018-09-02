from django.urls import path
from .views import ListNewsView

urlpatterns = [
path('news/', ListNewsView.as_view(), name='news-api')

]