from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    """
    Функция передает в браузер на страницу students_list.html словарь context со студентами
    и прикрепленными к ним преподователями 
    """
    template = 'school/students_list.html'
    obj_list = Student.objects.all().prefetch_related('teachers')
    context = {'object_list':obj_list}
    ordering = 'group'

    return render(request, template, context)
