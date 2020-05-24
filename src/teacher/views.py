from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse

from .forms import TeacherAddForm, TeacherEditForm
from .models import Teacher
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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

    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': qs, 'title': 'Teacher_list'}
    )


def teachers_add(request):
    if request.method == "POST":
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form, 'title': 'Teacher_add'}
    )


def teachers_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id {id} does not exist')

    if request.method == "POST":
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherEditForm(instance=teacher)

    return render(
        request=request,
        template_name='teachers_edit.html',
        context={'form': form, 'title': 'Teacher_edit', 'teacher': teacher}
    )
