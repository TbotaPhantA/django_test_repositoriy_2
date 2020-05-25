from django.shortcuts import render

# Create your views here.
def base_page(request):
    return render(request, template_name='rep_app/base.html')


def lessons_page(request):
    return render(request, template_name='rep_app/lessons.html')

def lesson_one_page(request):
    return render(request, template_name='rep_app/lessons/lesson_1.html')