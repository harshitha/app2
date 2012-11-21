from django.db import models

class Signal(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()

	def __unicode__(self):
		return self.title

class Choice(models.Model):
	signal = models.ForeignKey(Signal)
	choice = models.CharField(max_length=200)
	count = models.IntegerField()

	def __unicode__(self):
		return self.choice

