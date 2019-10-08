from django.db import models

# Create your models here.

class Genre(models.Model):
	genre = models.CharField(max_length=150)
	
	def __str__(self):
		return "%s: %s" % (self.id, self.genre)

class Platform(models.Model):
	platform = models.CharField(max_length=150)

	def __str__(self):
		return "%s: %s" % (self.id, self.platform)
	

class Developer(models.Model):
	developer = models.CharField(max_length=150)

	def __str__(self):
		return "%s: %s" % (self.id, self.developer)
	
class Games(models.Model):

	name = models.CharField(max_length=150)
	genre = models.ManyToManyField(Genre)
	platform = models.ManyToManyField(Platform)
	developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
	year = models.PositiveIntegerField()
	image = models.ImageField(null=False, blank=False)
	description = models.TextField()

	def __str__(self):
		return "%s: %s" % (self.id, self.name)
		

# Player name; {} , player age: {}{}“.format(name,age)