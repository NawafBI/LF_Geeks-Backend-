from django.db import models
from games.models import Game
from accounts.models import Profile
from games.models import Platform



# Create your models here.

class Guild(models.Model):
    name = models.CharField(max_length=150)
    games = models.ManyToManyField(Game)
    platform = models.ManyToManyField(Platform)
    tag = models.ImageField()
    description = models.TextField(max_length=5000)
    master = models.ForeignKey(Profile, on_delete=models.CASCADE)  #read the other options for on_delete        

    def __str__(self):
        return str(self.name)







 