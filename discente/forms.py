from dataclasses import field
from django import forms
from .models import Discente

class DiscenteForm(forms.ModelForm):

    class Meta:
        model = Discente
        fields = ("__all__")
