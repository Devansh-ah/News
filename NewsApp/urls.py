from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('general',views.general,name='general'),
    path('sports',views.sports,name='sports'),
    path('politics',views.politics,name='politics'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('music',views.music,name='music'),
    path('technology',views.technology,name='technology'),
    path('science',views.science,name='science'),
    path('business',views.business,name='business'),
    path('health',views.health,name='health'),
]