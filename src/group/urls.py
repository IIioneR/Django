from django.urls import path
from group.views import generate_groups, group_list, groups_add, groups_edit

app_name = 'groups'

urlpatterns = [
    path('generate-group/', generate_groups, name='generate'),
    path('', group_list, name='groups'),
    path('add/', groups_add),
    path('edit/<int:id>', groups_edit),
]
