from django.db import models

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=255, null=False)
	body = models.TextField(max_length=4000)
	url = models.TextField(max_length=255)
	god = models.CharField(max_length=255, default='')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title