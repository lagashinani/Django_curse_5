from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    ordering = 'group'
    context['object_list'] = Student.objects.all().order_by(ordering)

    return render(request, template, context)
