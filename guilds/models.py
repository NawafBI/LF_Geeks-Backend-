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

class Question(models.Model):
    title = models.TextField(max_length=250)
    active = models.BooleanField(default=False)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)

    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.modified = timezone.now()
    #     return super(Profile, self.save(*args, **kwargs))



    def __str__(self):
        return str(self.title)


# class Answer(models.Model):

#     def __str__(self):
#         return str(self.name)








 