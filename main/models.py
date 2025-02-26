from django.db import models


class Women(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField(blank=True)
	time_create = models.TimeField(auto_now_add=True)
	time_update = models.TimeField(auto_now=True)
	is_public = models.BooleanField(default=True)


	def __str__(self):
		return self.title


	class Meta:
		ordering = ['-time_update']