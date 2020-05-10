from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


# Create your views here.
def generate_students(request):
    for _ in range(10):
        Student.generate_student()
    qs = Student.objects.all()
    return HttpResponse(qs)


def students_list(request):
    qs = Student.objects.all()

    if request.GET.get("fname") or request.GET.get('lname'):
        qs = qs.filter(Q(first_name=request.GET.get("fname") | Q(last_name=request.GET.get("lname"))))

    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': qs, 'title': 'Student_list'}
    )


def students_add(request):
    if request.method == "POST":
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form, 'title': 'Student_add'}
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id {id} does not exist')

    if request.method == "POST":
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_edit.html',
        context={'form': form, 'title': 'Student_edit'}
    )


def students_delete(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id {id} does not exist')

    if request.method == "POST":
        del_student = student.delete()
        print(f'{del_student}have deleted')
        return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_del.html',
        context={'form': form, 'title': 'Student_del'}
    )
