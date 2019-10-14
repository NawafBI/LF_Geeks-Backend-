from django.db import models
from games.models import Game
from accounts.models import Profile
from games.models import Platform


# add members
# Create your models here.

class Guild(models.Model):
    name = models.CharField(max_length=150)
    games = models.ManyToManyField(Game)
    platform = models.ManyToManyField(Platform)
    tag = models.ImageField()
    description = models.TextField(max_length=5000)
    # read the other options for on_delete
    master = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    title = models.TextField(max_length=250)
    active = models.BooleanField(default=False)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


# class Answer(models.Model):

#     def __str__(self):
#         return str(self.name)
