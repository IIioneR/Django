from django.urls import path
from teacher.views import generate_teachers, teachers_list, teachers_add, teachers_edit

urlpatterns = [
    path('', teachers_list, name='teachers'),
    path('add/', teachers_add),
    path('edit/<int:id>', teachers_edit),
    path('gen-teachers/', generate_teachers),
]