from django.urls import path
from . import views
urlpatterns = [
    #path('min/',views.Min,name='home' ),
    path('recipe/',views.Recipe1.as_view(),name='min'),
    path('',views.home,name='index'),
    path('minseller',views.minseller,name='minimum')
]