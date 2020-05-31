from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student


# Create your views here.
def generate_students(request):
    for _ in range(10):
        Student.generate_student()
    qs = Student.objects.all()
    return HttpResponse(qs)


def students_list(request):
    qs = Student.objects.all().select_related('group')

    if request.GET.get("fname") or request.GET.get('lname'):
        qs = qs.filter(Q(first_name=request.GET.get("fname")) | Q(last_name=request.GET.get("lname")))

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
            return HttpResponseRedirect(reverse('students:list'))
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
            return HttpResponseRedirect(reverse('students:list'))
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
        form = StudentDeleteForm(request.POST, instance=student)
        if form.is_valid():
            del_student = student.delete()
            print(f'Student {del_student} have deleted')
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentDeleteForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_del.html',
        context={'form': form, 'title': 'Student_del'}
    )


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')
        if request.GET.get("fname") or request.GET.get('lname'):
            qs = qs.filter(Q(first_name=request.GET.get("fname")) | Q(last_name=request.GET.get("lname")))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Student list'
        return context


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit Student'
        return context


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students_del.html'
    form_class = StudentDeleteForm

    def get_success_url(self):
        return reverse('students:list')
