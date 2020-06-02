from django.contrib import admin
from django.db.models import Count

from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')
    list_select_related = ['group']


admin.site.register(Student, StudentAdminModel)
