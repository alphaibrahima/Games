"""
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from mot_de_passe import views
from django.urls import path

urlpatterns = [
    path('', views.mot_de_passe, name='mot_de_passe'),
    path('scores', views.scores_view, name='scores_mdp'),
    path('test', views.score_update, name='score_update'),
    path('proposition_mdp', views.proposition, name='proposition_mdp'),
    path('add_feedback', views.add_feedback, name='add_feedback')

    
]