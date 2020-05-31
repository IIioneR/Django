from django.core.exceptions import ValidationError
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    pass


class StudentEditForm(StudentBaseForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.all().filter(email=email).exists():
            raise ValidationError('Email is already exists')

        return email


class StudentDeleteForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = []
