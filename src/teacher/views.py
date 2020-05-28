from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import TeacherAddForm, TeacherEditForm, TeacherDeleteForm
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


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teacher list'
        return context


class TeachersUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersCreateView(CreateView):
    model = Teacher
    template_name = 'teachers_add.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers_delete.html'
    form_class = TeacherDeleteForm

    def get_success_url(self):
        return reverse('teachers:list')
