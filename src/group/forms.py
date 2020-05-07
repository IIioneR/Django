from django.forms import ModelForm

from group.models import Group


class GroupAddForms(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
