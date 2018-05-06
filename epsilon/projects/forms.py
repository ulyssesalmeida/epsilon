from django import forms
from epsilon.projects.models import Pip


class PipForm(forms.ModelForm):
    class Meta:
        model = Pip
        exclude = ('pipId',)