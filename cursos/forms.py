from dataclasses import field
from django import forms
from post.models import Curso

class CursosForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ("__all__")
