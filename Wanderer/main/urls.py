from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="home"),
  path('populartours', views.populartours, name="poptours"),
  path('tourselect', views.tourselect, name="tourselect"),
  path('about', views.about, name="about"),
  path('likepost/', views.likePost, name='likepost'),
  path('dislikepost/', views.dislikePost, name='dislikepost')
]
