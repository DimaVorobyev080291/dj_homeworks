from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Админка модели Student
    """
    list_display = ['name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
