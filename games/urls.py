from django.urls import path
from .views import GameDetailAPIView, GameCreateAPIView, GameListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('creategame/', GameCreateAPIView.as_view(), name='create-game'),
    path('detailgame/', GameDetailAPIView.as_view(), name='detail-game'),
    path('gamelist/', GameListView.as_view(), name='game-list'),
]



urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
