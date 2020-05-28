
from django.urls import path
from student.views import generate_students, \
    StudentsListView, StudentsUpdateView, StudentsCreateView, StudentDeleteView

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),
    path('add/', StudentsCreateView.as_view(), name='add'),
    path('edit/<int:pk>', StudentsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete'),
    path('generate-students/', generate_students),

]
