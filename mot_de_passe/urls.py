
from mot_de_passe import views
from django.urls import include, path
from rest_framework import routers, viewsets

# API Django Rest
router = routers.DefaultRouter()
router.register(r'mots', views.MotsViewSet)
router.register(r'scoresapi', views.ScoreViewSet)
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'contreun', views.ContreUnViewSet)
router.register(r'scoreun', views.ScoreTwoViewSet)

urlpatterns = [
    path('', views.mot_de_passe, name='mot_de_passe'),
    path('scores', views.scores_view, name='scores_mdp'),
    path('test', views.score_update, name='score_update'),
    path('proposition_mdp', views.proposition, name='proposition_mdp'),
    path('add_feedback', views.add_feedback, name='add_feedback'),

    # mode un contre un
    path('modeun', views.modeOne, name='modeun'),
    path('invite/<int:id>/', views.Invit, name = 'invit' ),
    path('show', views.ShowInvi, name = 'show'),
    path('show/<int:id>/', views.AccpetInv, name = 'accept'),
    path('1vs1/', views.jeu1vs1, name='1vs1'),
    path('jeu1Sall/', views.jeu1vs1, name='jeu1Sall'),

    # API Django Rest
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    

    
]