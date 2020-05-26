from django.shortcuts import render

# Create your views here.
def base_page(request):
    return render(request, template_name='rep_app/base.html')


def lessons_page(request):
    return render(request, template_name='rep_app/lesson_list.html')


def lesson_one_page(request):
    return render(request, template_name='rep_app/lessons/lesson_1.html')


def lessons_true_page(request):
    return render(request, template_name='rep_app/lessons_true.html')


def lessons_custom_page(request):
    return render(request, template_name='rep_app/lessons_custom.html')


def lessons_battle_page(request):
    return render(request, template_name='rep_app/lessons_battle.html')