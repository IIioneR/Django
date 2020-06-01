from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse, reverse_lazy
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


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'
    login_url = reverse_lazy('login')
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        if request.GET.get("fname") or request.GET.get('lname'):
            qs = qs.filter(Q(first_name=request.GET.get("fname")) | Q(last_name=request.GET.get("lname")))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teacher list'
        return context


class TeachersUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers_add.html'
    form_class = TeacherAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('teachers:list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers_delete.html'
    form_class = TeacherDeleteForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('teachers:list')
