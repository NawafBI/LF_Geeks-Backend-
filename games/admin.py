from django.contrib import admin
from .models import Game, Developer, Platform, Genre

# Register your models here.
admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Platform)
admin.site.register(Genre)