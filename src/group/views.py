from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse

from .forms import GroupEditForm, GroupAddForm
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
            return HttpResponseRedirect(reverse('groups'))
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
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupEditForm(instance=group)

    return render(
        request=request,
        template_name='groups_edit.html',
        context={'form': form, 'title': 'Group_edit', 'group': group}
    )
