from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('video', views.video),
    path('guide', views.guide),
    path('course_detail', views.course_detail),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'), 
]