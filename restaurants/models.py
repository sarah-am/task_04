from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __str__(self):
		# return self.name
		# return ("%s, %H:%M:%S, %H:%M:%S") % (self.name, self.opening_time, self.closing_time)
		return "%s, %s, %s" % (self.name, self.opening_time, self.closing_time)
