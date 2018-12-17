from django.db import models


class Contact(models.Model):
	subject = models.CharField(max_length=264)
	email = models.EmailField(unique=True)
	text = models.TextField()

	
	def __str__(self):
		return self.email

	def __repr__(self):
		return "<Contact {}>".format(self.email)


