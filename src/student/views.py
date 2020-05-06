from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student.forms import StudentAddForm
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

    result = "<br>".join(str(student) for student in qs)
    # return HttpResponse(result)
    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': result}
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
        context={'form': form}
    )
