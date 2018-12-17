from django.db import models




class Product(models.Model):
	name = models.CharField(max_length=264)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	description = models.TextField()
	image = models.ImageField(default='static/images/image.png' , upload_to='static/images/')


	def __str__(self):
		return self.name

	# def __repr__(self):
	# 	return "<Product {}>".format(self.name)


class Client(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField(max_length=264, unique=True)
	password = models.CharField(max_length=264)
	# products = models.ForeignKey(Product, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='static/images/image.png', upload_to='static/images/profile_pic')

						
		
	def __str__(self):
		return self.first_name

	def __repr__(self):
		return "<Client {}>".format(self.first_name)


# class Maillots(models.Model):	











