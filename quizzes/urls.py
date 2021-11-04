from django.urls import path
from .views import(
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    Score,
)

app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main_view'),
    path('score', Score, name='score'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]