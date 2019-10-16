from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from .views import GuildView, QuestionCreateAPIView, QuestionsView, QuestionsUpdateView, AnswerAPIView, RecruitmentView


router = SimpleRouter()
router.register("guild", GuildView)


urlpatterns = [
    path('', include(router.urls)),
    path('question_create/', QuestionCreateAPIView.as_view()),
    path('question_list/', QuestionsView.as_view()),
    path('question_update/<int:question_id>/', QuestionsUpdateView.as_view()),
    path('answer/', AnswerAPIView.as_view()),
    path('recruitment/<int:recruitment_id>/', RecruitmentView.as_view()),

]




if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
