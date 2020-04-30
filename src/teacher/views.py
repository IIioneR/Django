from .models import Teacher
from django.http import HttpResponse

# Create your views here.


def generate_teachers(request):
    for _ in range(10):
        Teacher.generate_teacher()
    qs = Teacher.objects.all()
    return HttpResponse(qs)
