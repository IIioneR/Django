from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from .forms import GroupEditForm, GroupAddForm, GroupDeleteForm
from .models import Group
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render


def generate_groups(request):
    for _ in range(10):
        Group.generate_group()
    qs = Group.objects.all()
    return HttpResponse(qs)


def group_list(request):
    qs = Group.objects.all()

    if request.GET.get("name_group") or request.GET.get('number_of_group'):
        qs = qs.filter(Q(name_group=request.GET.get("name_group")) | Q(
            number_of_group=request.GET.get("number_of_group")))

    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': qs, 'title': 'Group_list'}
    )


def groups_add(request):
    if request.method == "POST":
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='groups_add.html',
        context={'form': form, 'title': 'Group_add'}
    )


def groups_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id {id} does not exist')

    if request.method == "POST":
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupEditForm(instance=group)

    return render(
        request=request,
        template_name='groups_edit.html',
        context={'form': form, 'title': 'Group_edit', 'group': group}
    )


class GroupsListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'
    login_url = reverse_lazy('login')
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('teacher')
        qs = qs.order_by('-id')
        if request.GET.get("name_group") or request.GET.get('number_of_group'):
            qs = qs.filter(Q(name_group=request.GET.get("name_group")) | Q(number_of_group=request.GET.get("number_of_group")))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group_list'
        return context


class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups_delete.html'
    form_class = GroupDeleteForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')
