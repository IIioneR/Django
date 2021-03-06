from django.urls import path
from group.views import generate_groups, GroupsListView, GroupsUpdateView, \
    GroupsCreateView, GroupDeleteView

app_name = 'groups'

urlpatterns = [
    path('generate-group/', generate_groups),
    path('', GroupsListView.as_view(), name='list'),
    path('add/', GroupsCreateView.as_view(), name='add'),
    path('edit/<int:pk>', GroupsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', GroupDeleteView.as_view(), name='delete'),
]
