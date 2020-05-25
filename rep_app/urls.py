from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page, name='base_page'),
    path('lessons', views.lessons_page, name='lessons_name'),
    path('lesson1', views.lesson_one_page, name='lesson_one_page'),
]