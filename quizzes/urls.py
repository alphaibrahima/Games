from django.urls import path, include
from rest_framework import routers, viewsets
from .views import(
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    Score,

    # Viewset of Api
    QuizViewSet,
    AnswerViewSet,
    ResultViewSet,
    QuestionViewSet,
)
# API Django Rest
router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'resultat', ResultViewSet)




app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main_view'),
    path('score', Score, name='score'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),


        # API Django Rest
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]