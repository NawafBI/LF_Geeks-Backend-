from django.db import models

# Create your models here.

class Genre(models.Model):
	GENRE_CHOICES=[
		('Action','Action'),
		('Adventure','Adventure'),
		('RPG','RPG'),
		('Multiplayer','Multiplayer')
	]
	genre = models.CharField(max_length=150 , choices=GENRE_CHOICES)
	
	def __str__(self):
		return "%s: %s" % (self.genre, self.platform)

class Platform(models.Model):
	PLATFORM_CHOICES=[
		('Playstation 4','Playstation 4'),
		('PC','PC'),
		('XBOX-ONE','XBOX-ONE'),
		('Nintendo','Nintendo')
	]
	platform = models.CharField(max_length=150, choices=PLATFORM_CHOICES)

	def __str__(self):
		return "%s: %s" % (self.id, self.platform)
	
class Games(models.Model):
	DEVELOPER_CHOICES=[
		('Blizzard','Blizzard'),
		('SONY','SONY'),
		('EA','EA'),
	]
	name = models.CharField(max_length=150)
	genre = models.ManyToManyField(Genre)
	platform = models.ManyToManyField(Platform)
	developer = models.CharField(max_length=150 , choices=DEVELOPER_CHOICES)
	year = models.PositiveIntegerField()
	image = models.ImageField(null=False, blank=False)
	description = models.TextField()

	def __str__(self):
		return "%s: %s" % (self.id, self.name)
