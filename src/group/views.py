from django.db.models import Q

from .models import Group
from django.http import HttpResponse
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

    result = "<br>".join(str(group) for group in qs)
    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': result}
    )
