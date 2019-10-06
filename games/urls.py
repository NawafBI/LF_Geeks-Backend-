from django.urls import path
from .views import GameCreateAPIView, GameView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('creategame/', GameCreateAPIView.as_view(), name='create-game'),
    path('gamelist/', GameView.as_view(), name='game-list'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
