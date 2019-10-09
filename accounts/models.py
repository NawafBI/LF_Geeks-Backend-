from django.db import models
from games.models import Game
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)	
  image = models.ImageField()
  age = models.PositiveIntegerField()
  cv = models.TextField(max_length=300)
  games = models.ManyToManyField(Game)
  # guilds = models.ManyToManyField(related_name=guilds)


  def __str__(self):
    return "%s: %s" % (self.id, self.user)
      


@receiver(post_save, sender=User)
def profile_creation(instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, age=0)




