from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Milestone(models.Model):
	owner		 = models.ForeignKey('auth.User', related_name='milestones', on_delete=models.CASCADE)
	title  		 = models.CharField(max_length=254)
	description  = models.TextField()
	start_date   = models.DateTimeField(auto_now_add=True)
	due_date	 = models.DateTimeField()
	complete	 = models.BooleanField()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title