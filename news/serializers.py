from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'title', 'body', 'created_at')