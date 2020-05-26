from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page, name='base_page'),
    path('lessons', views.lessons_page, name='lessons_name'),
    path('lesson1', views.lesson_one_page, name='lesson_one_page'),
    path('lesson_true', views.lessons_true_page, name='lessons_true_page'),
    path('lesson_custom', views.lessons_custom_page, name='lessons_custom_page'),
    path('lesson_battle', views.lessons_battle_page, name='lessons_battle_page'),
]