from django.db.models import Q

from .models import Teacher
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def generate_teachers(request):
    for _ in range(10):
        Teacher.generate_teacher()
    qs = Teacher.objects.all()
    return HttpResponse(qs)


def teachers_list(request):
    qs = Teacher.objects.all()

    if request.GET.get("fname") or request.GET.get('lname') or request.GET.get('email'):
        qs = qs.filter(Q(first_name=request.GET.get("fname")) | Q(
            last_name=request.GET.get("lname")) | Q(
            email=request.GET.get("email")))

    result = "<br>".join(str(teacher) for teacher in qs)
    # return HttpResponse(result)
    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': result}
    )
