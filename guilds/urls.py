from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from .views import GuildView


router = SimpleRouter()
router.register("guild", GuildView)


urlpatterns = [
    path('', include(router.urls)),
    #  path('/', views.ProfileViewSet.as_view()),
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
