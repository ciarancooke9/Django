from django.urls import path
from . import views


urlpatterns = [
    path('addactor/', views.addactor_view, name='add_actor'),
    path('addshow/', views.addshow_view, name='home'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),

]
