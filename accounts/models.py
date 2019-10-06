from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)	
    image = models.ImageField()
    age = models.PositiveIntegerField()


    def __str__(self):
        return str(self.user.first_name)

@receiver(post_save, sender=User)
def profile_creation(instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, age=0)



